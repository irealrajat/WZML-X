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
            self.MirrorCommand.extend([f'unzipmirrorx{CMD_SUFFIX}', f'uzmx{CMD_SUFFIX}', f'zipmirrorx{CMD_SUFFIX}', f'zmx{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirrorx{CMD_SUFFIX}', f'quzmx{CMD_SUFFIX}', f'qbzipmirrorx{CMD_SUFFIX}', f'qzmx{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip{CMD_SUFFIX}', f'yz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleechx{CMD_SUFFIX}', f'uzlx{CMD_SUFFIX}', f'zipleechx{CMD_SUFFIX}', f'zlx{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleechx{CMD_SUFFIX}', f'quzlx{CMD_SUFFIX}', f'qbzipleechx{CMD_SUFFIX}', f'qzlx{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleechx{CMD_SUFFIX}', f'yzlx{CMD_SUFFIX}'])
        self.CloneCommand = [f'clonex{CMD_SUFFIX}', f'cx{CMD_SUFFIX}']
        self.CountCommand = f'countx{CMD_SUFFIX}'
        self.DeleteCommand = f'delx{CMD_SUFFIX}'
        self.CancelMirror = f'cancelx{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelallx{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'listx{CMD_SUFFIX}'
        self.SearchCommand = f'searchx{CMD_SUFFIX}'
        self.StatusCommand = [f'statusx{CMD_SUFFIX}', f'sx{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'usersx{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorizex{CMD_SUFFIX}', f'ax{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorizex{CMD_SUFFIX}', f'uax{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklistx{CMD_SUFFIX}', f'blx{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklistx{CMD_SUFFIX}', f'rblx{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudox{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudox{CMD_SUFFIX}'
        self.PingCommand = [f'pingx{CMD_SUFFIX}', f'px{CMD_SUFFIX}']
        self.RestartCommand = [f'restartx{CMD_SUFFIX}', f'rx{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'statsx{CMD_SUFFIX}', f'stx{CMD_SUFFIX}']
        self.HelpCommand = f'helpx{CMD_SUFFIX}'
        self.LogCommand = f'logx{CMD_SUFFIX}'
        self.ShellCommand = f'shellx{CMD_SUFFIX}'
        self.EvalCommand = f'evalx{CMD_SUFFIX}'
        self.ExecCommand = f'execx{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocalsx{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsettingx{CMD_SUFFIX}', f'bsx{CMD_SUFFIX}']
        self.UserSetCommand = [f'usettingx{CMD_SUFFIX}', f'usx{CMD_SUFFIX}']
        self.BtSelectCommand = f'btselx{CMD_SUFFIX}'
        self.CategorySelect = f'ctselx{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtestx{CMD_SUFFIX}', f'spx{CMD_SUFFIX}']
        self.RssCommand = f'rssx{CMD_SUFFIX}'
        self.LoginCommand = 'loginx'
        self.AddImageCommand = f'addimgx{CMD_SUFFIX}'
        self.ImagesCommand = f'imagesx{CMD_SUFFIX}'
        self.IMDBCommand = f'imdbx{CMD_SUFFIX}'
        self.AniListCommand = f'animex{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelpx{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfox{CMD_SUFFIX}', f'mix{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdlx{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdcleanx{CMD_SUFFIX}', f'gcx{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcastx{CMD_SUFFIX}', f'bcx{CMD_SUFFIX}']

BotCommands = _BotCommands()
