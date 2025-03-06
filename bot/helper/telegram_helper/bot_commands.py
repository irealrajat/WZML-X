#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirrorx{CMD_SUFFIX}', f'mx{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirrorx{CMD_SUFFIX}', f'qmx{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdlx{CMD_SUFFIX}', f'yx{CMD_SUFFIX}']
        self.LeechCommand = [f'leechx{CMD_SUFFIX}', f'lx{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleechx{CMD_SUFFIX}', f'qlx{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleechx{CMD_SUFFIX}', f'ylx{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirrorx{CMD_SUFFIX}', f'uzmx{CMD_SUFFIX}', f'zipmirror{CMD_SUFFIX}', f'zm{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirrorx{CMD_SUFFIX}', f'quzmx{CMD_SUFFIX}', f'qbzipmirror{CMD_SUFFIX}', f'qzm{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzipx{CMD_SUFFIX}', f'yzx{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleechx{CMD_SUFFIX}', f'uzlx{CMD_SUFFIX}', f'zipleech{CMD_SUFFIX}', f'zl{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleechx{CMD_SUFFIX}', f'quzlx{CMD_SUFFIX}', f'qbzipleech{CMD_SUFFIX}', f'qzl{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleechx{CMD_SUFFIX}', f'yzlx{CMD_SUFFIX}'])
        self.CloneCommand = [f'clonex{CMD_SUFFIX}', f'cx{CMD_SUFFIX}']
        self.CountCommand = f'countx{CMD_SUFFIX}'
        self.DeleteCommand = f'delx{CMD_SUFFIX}'
        self.CancelMirror = f'cancelx{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelallx{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'listx{CMD_SUFFIX}'
        self.SearchCommand = f'searchx{CMD_SUFFIX}'
        self.StatusCommand = [f'statusx{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'usersx{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorizex{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorizex{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudox{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudox{CMD_SUFFIX}'
        self.PingCommand = [f'pingx{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restartx{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'statsx{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'helpx{CMD_SUFFIX}'
        self.LogCommand = f'logx{CMD_SUFFIX}'
        self.ShellCommand = f'shellx{CMD_SUFFIX}'
        self.EvalCommand = f'evalx{CMD_SUFFIX}'
        self.ExecCommand = f'execx{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsettingx{CMD_SUFFIX}', f'bsx{CMD_SUFFIX}']
        self.UserSetCommand = [f'usettingx{CMD_SUFFIX}', f'usx{CMD_SUFFIX}']
        self.BtSelectCommand = f'btselx{CMD_SUFFIX}'
        self.CategorySelect = f'ctselx{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtestx{CMD_SUFFIX}', f'spx{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
