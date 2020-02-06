import easycli


class MarkdownServer(easycli.Root):
    __help__ = 'Markdown Server'
    __completion__ = True
    __arguments__ = [
        easycli.Argument(
            '-v', '--version',
            action='store_true',
            help='Show version'
        ),
    ]

    def __call__(self, args):
        if args.version:
            from markdownserver import __version__
            print(__version__)
            return

        return super().__call__(args)