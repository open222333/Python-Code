# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import os
import urllib

from flask import Flask, jsonify, Response
from flask_cache import Cache
from flask_mail import Mail
from flask_babel import Babel
from flask_mongoengine import MongoEngine
from flask_mongoengine.json import MongoEngineJSONEncoder
from pymongo import MongoClient
from .reverseproxied import ReverseProxied
from raven.contrib.flask import Sentry
from flask_pymongo import PyMongo
from . import converters
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy

__version__ = '1.0.0'
__all__ = ('cache', 'caches', 'mongo')

caches = {
    'default': Cache()
}
cache = caches['default']
sentry = Sentry()
mail = Mail()
babel = Babel()

mongo = MongoEngine()
logmongo = PyMongo()
mysql = MySQL()
sqlalchemy = SQLAlchemy()


def create_application(settings=None):
    app = Flask('test', static_folder="../static")
    app.wsgi_app = ReverseProxied(app.wsgi_app)
    app.config.from_object('test.settings.defaults')
    if os.environ.get('SETTINGS_MODULE'):
        app.config.from_object(os.environ.get('SETTINGS_MODULE'))
    if settings is not None:
        if isinstance(settings, dict):
            app.config.update(settings)
        else:
            app.config.from_object(settings)

    def init_caches(app, caches):
        for name, cache in caches.items():
            def config():
                uri = urllib.parse.urlparse(
                    os.environ.get('CACHE_URL_{name}'.format(
                        name=name).upper(), 'null://')
                )
                query = dict(urllib.parse.parse_qsl(uri.query))

                yield 'CACHE_TYPE', uri.scheme
                if 'timeout' in query:
                    yield 'CACHE_DEFAULT_TIMEOUT', int(query['timeout'])
                if 'threshold' in query:
                    yield 'CACHE_THRESHOLD', int(query['threshold'])
                if uri.scheme == 'redis':
                    yield 'CACHE_REDIS_HOST', uri.hostname
                    if uri.port:
                        yield 'CACHE_REDIS_PORT', uri.port
                    if uri.password:
                        yield 'CACHE_REDIS_PASSWORD', uri.password
                    yield 'CACHE_REDIS_DB', uri.path.lstrip('/')
                elif uri.scheme in ['memcached', 'gaememcached', 'saslmemcached']:
                    yield 'CACHE_MEMCACHED_SERVERS', [uri.netloc]

                    if uri.scheme == 'saslmemcached':
                        if uri.username:
                            yield 'CACHE_MEMCACHED_USERNAME', uri.username
                        if uri.password:
                            yield 'CACHE_MEMCACHED_PASSWORD', uri.password
                elif uri.scheme == 'filesystem':
                    yield 'CACHE_DIR', uri.netloc.hostname + uri.path

            cache.init_app(app, config=dict(config()))

    def init_sentry(app, sentry):
        sentry.init_app(app)

    def init_mail(app, mail):
        mail.init_app(app)

    def init_babel(app, babel):
        babel.init_app(app)

    def init_mongo(app, mongo):
        mongo.init_app(app)

    def init_log(app, logmongo):
        logmongo.init_app(app, config_prefix='LOGMONGO')

    def init_mysql(app, mysql):
        mysql.init_app(app)

    def init_sqlalchemy(app, sqlalchemy):
        sqlalchemy.init_app(app)

    init_mongo(app, mongo)
    init_caches(app, caches)
    init_sentry(app, sentry)
    init_mail(app, mail)
    init_babel(app, babel)
    init_log(app, logmongo)
    init_mysql(app, mysql)
    init_sqlalchemy(app, sqlalchemy)

    app.url_map.converters['objectid'] = converters.Base64ObjectIDConverter
    app.json_encoder = type(
        'JSONEncoder', (converters.JSONEncoder, MongoEngineJSONEncoder), {})

    # Register blueprints
    import test.api.a1
    app.register_blueprint(test.api.a1.application, url_prefix='/a1')
    import test.api.a2
    app.register_blueprint(test.api.a2.application, url_prefix='/a2')

    @app.route('/', methods=['GET'], strict_slashes=False)
    def index():
        return "ok", 200

    @app.route('/.well-known/apple-app-site-association', methods=['GET'], strict_slashes=False)
    @app.route('/apple-app-site-association', methods=['GET'], strict_slashes=False)
    def apple():
        content_type = 'application/pkcs7-mime'
        content = '{"applinks":{"apps":[],"details":[{"appID":"88JHT77439.com.rhz-inhouse.app1","paths":["/video/share/*"]},{"appID":"T4LE5YB736.com.avn-inhouse.app1","paths":["/video/share/*"]},{"appID":"VTBL6RXPE5.com.avn2-inhouse.app1","paths":["/video/share/*"]}]}}'
        return Response(content, mimetype=content_type)

    @app.route('/.well-known/assetlinks.json', methods=['GET'], strict_slashes=False)
    @app.route('/assetlinks.json', methods=['GET'], strict_slashes=False)
    def android_json():
        content_type = 'application/json'
        content = '[{"relation":["delegate_permission/common.handle_all_urls"],"target":{"namespace":"android_app","package_name":"com.test","sha256_cert_fingerprints":["4D:16:C3:4C:49:1C:9E:6C:A6:05:24:F7:C1:39:F7:41:27:D9:CC:8B:70:25:83:80:A4:0F:27:4E:A5:62:EA:78"]}}]'
        return Response(content, mimetype=content_type)

    client = MongoClient()

    from . import signals

    app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
    return app


def create_application_backend(settings=None):
    app = create_application(settings)
    import test.backend
    app.register_blueprint(test.backend.application, url_prefix='/backend')
    return app
