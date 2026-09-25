import structlog


def logger_config():
    """
    This is a basic logger setup ,
    we will implement upgrades later-on
    """
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.dev.ConsoleRenderer(pad_level=False),
        ],
    )
    return structlog


logger = logger_config().getLogger()
