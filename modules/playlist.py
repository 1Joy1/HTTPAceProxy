# -*- coding: utf-8 -*-
class PlaylistConfig():

    # Default playlist format
    m3uemptyheader = '#EXTM3U\n'
    m3uheader = '#EXTM3U deinterlace=1 m3uautoload=1 cache=1000\n'
    # If you need the #EXTGRP field put this #EXTGRP:%(group)s\n after %(name)s\n.
    m3uchanneltemplate = \
       '#EXTINF:-1 group-title="%(group)s" tvg-name="%(tvg)s" tvg-id="%(tvgid)s" tvg-logo="%(logo)s",%(name)s\n#EXTGRP:%(group)s\n%(url)s\n'

    # Channel names mapping. You may use this to rename channels.
    m3uchannelnames = dict()
    # Examples:
    m3uchannelnames['Amedia 1'] = 'A1'
    m3uchannelnames['Amedia 2'] = 'A2'
    m3uchannelnames['Da Vinci Learning'] = 'Da Vinci'
    m3uchannelnames['SET'] = 'Sony channel'
    m3uchannelnames['SET HD'] = 'Sony channel HD'
    m3uchannelnames['History 2 HD'] = 'H2 HD'
    m3uchannelnames['5 канал'] = 'Пятый канал'
    m3uchannelnames['TV XXI (TV21)'] = 'TV XXI'
    m3uchannelnames['TV1000 Action East'] = 'TV 1000 Action'
    m3uchannelnames['TV 1000 Action East'] = 'TV 1000 Action'
    m3uchannelnames['TV1000 Русское кино'] = 'TV 1000 Русское кино'
    m3uchannelnames['Enter Film'] = 'Enter-фильм'
    m3uchannelnames['Кинопоказ 1 HD'] = 'Кинопоказ HD-1'
    m3uchannelnames['Кинопоказ 2 HD'] = 'Кинопоказ HD-2'
    m3uchannelnames['Travel+Adventure'] = 'Travel + adventure'
    m3uchannelnames['Travel + adventure HD'] ='Travel+Adventure HD'
    m3uchannelnames['HD Life'] = 'HDL'
    m3uchannelnames['ID Xtra'] = 'ID Investigation Discovery'
    m3uchannelnames['Первый'] = 'Первый канал'
    m3uchannelnames['ТВ3'] = 'ТВ 3'
    m3uchannelnames['КХЛ'] = 'КХЛ ТВ'
    m3uchannelnames['Канал Disney'] = 'Disney Channel'
    m3uchannelnames['Boomerаng TV'] = 'Boomerаng'
    m3uchannelnames['Nick Jr.'] = 'Nick Jr'
    m3uchannelnames['Бобёр']  = 'Бобер'
    m3uchannelnames['Наука'] = 'Наука 2.0'
    m3uchannelnames['Russian Travel Guide'] = 'RTG TV'
    m3uchannelnames['Иллюзион +'] = 'Иллюзион+'
    m3uchannelnames['РТВ - Любимое кино'] = 'Наше Любимое Кино'
    m3uchannelnames['ТВ Центр'] = 'ТВЦ'
    m3uchannelnames['UA:Крим'] = 'UA Крим'
    m3uchannelnames['UA:Перший'] = 'UA Перший'
    m3uchannelnames['UA:Культура'] = 'UA Культура'
    m3uchannelnames['UA:TV'] = 'UA TV'
    m3uchannelnames['UA:Житомир'] = 'UA Житомир'
    m3uchannelnames['VH1'] = 'VH1 European'
    m3uchannelnames['1 HD'] = '1HD Music Television'
    m3uchannelnames['1Music (Hungary)'] = '1 Music Channel (Hungary)'

    # Similar to m3uchannelnames but for groups
    m3ugroupnames = dict()

    # Channel name to tvg name mappings.
    m3utvgnames = dict()
    # m3utvgnames['Channel name'] = 'Tvg_name'

    # Playlist sorting options.
    sort = False
    sortByName = False
    sortByGroup = False

    # This comparator is used for the playlist sorting.
    @staticmethod
    def sortItems(itemlist):
        if PlaylistConfig.sortByGroup: return sorted(itemlist, key=lambda x:x['group'])
        elif PlaylistConfig.sortByName: return sorted(itemlist, key=lambda x:x['name'])
        else: return itemlist

    # This method can be used to change a channel info such as name, group etc.
    # The following fields can be changed:
    #
    #    name - channel name
    #    url - channel URL
    #    tvg - channel tvg name
    #    tvgid - channel tvg id
    #    group - channel group
    #    logo - channel logo
    @staticmethod
    def changeItem(item):
        PlaylistConfig._changeItemByDict(item, 'name', PlaylistConfig.m3uchannelnames)
        PlaylistConfig._changeItemByDict(item, 'group', PlaylistConfig.m3ugroupnames)
        PlaylistConfig._changeItemByDict(item, 'name', PlaylistConfig.m3utvgnames, 'tvg')

    @staticmethod
    def _changeItemByDict(item, key, replacementsDict, setKey=None):
        if len(replacementsDict) > 0:
            value = item[key]
            if not setKey: setKey = key

            if type(value) == str:
                value = replacementsDict.get(value)
                if value: item[setKey] = value
            elif type(value) == unicode:
                value = replacementsDict.get(value.encode('utf-8'))
                if value: item[setKey] = value.decode('utf-8')

    xml_template = """<?xml version="1.0" encoding="utf-8"?>
    <items>
    <playlist_name>Playlist</playlist_name>

    %(items)s

    </items>
    """

    xml_channel_template = """
    <channel>
      <title><![CDATA[%(title)s]]></title>
      <description><![CDATA[<tr><td>%(description_title)s</td></tr>]]></description>
      <playlist_url>%(hostport)s%(url)s</playlist_url>
    </channel>
    """

    xml_stream_template = """
    <channel>
      <title><![CDATA[%(title)s]]></title>
      <description><![CDATA[<tr><td>%(description_title)s</td></tr>]></description>
      <stream_url><![CDATA[%(hostport)s%(url)s]]></stream_url>
    </channel>
    """
