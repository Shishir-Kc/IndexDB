import argparse
import asyncio


async def test():
    print("hello world")


async def build_parser():
    parser = argparse.ArgumentParser(prog="IndexDB")
    subparser = parser.add_subparsers(dest="commands")

    testt = subparser.add_parser("test", description="test")
    testt.set_defaults(func=test)

    return parser


if __name__ == "__main__":
    parser = asyncio.run(build_parser())
    args = parser.parse_args()
    if hasattr(args, "func"):
        asyncio.run(args.func())
