from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    lineID = models.TextField()
    nickname = models.TextField()
    createDate = models.DateTimeField()

    def isInUserData(self, userId):
        '''檢查lineID是否存在 User'''
        return User.objects.filter(lineID=userId).exists()

    def addUserData(self, userId, nickname):
        '''添加使用者至資料表 User'''
        addDataTemp = User(
            lineID=userId,
            nickname=nickname,
            createDate=str(datetime.now())[:-7]
        )
        addDataTemp.save()


class Group(models.Model):
    groupID = models.TextField()
    createDate = models.DateTimeField()

    def isInGroupData(self, groupId):
        '''檢查groupID是否存在 Group'''
        return Group.objects.filter(groupID=groupId).exists()

    def addGroupData(self, groupId):
        '''添加群組ID至資料表 Group'''
        addDataTemp = Group(
            groupID=groupId,
            createDate=str(datetime.now())[:-7]
        )
        addDataTemp.save()


class Association(models.Model):
    lineID = models.TextField()
    groupID = models.TextField()

    def isInAssociationData(self, userId, groupId):
        '''檢查AssociationData是否存在'''
        lineIDExists = Association.objects.filter(lineID=userId).exists()
        groupIDExists = Association.objects.filter(groupID=groupId).exists()
        return (lineIDExists and groupIDExists)

    def addAssociationData(self, userId, groupId):
        '''建立在關聯表 Association'''
        addAssociationDataTemp = Association(
            lineID=userId,
            groupID=groupId
        )
        addAssociationDataTemp.save()
