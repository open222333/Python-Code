def init_app(app):
    @app.route('/auth')
    def auth():
        return 'auth'
