import os


def main(token):
    from vkbottle import Bot, load_blueprints_from_package

    token = "fdb90ff2dbec36a79ac5b079f58c8c750a3298246753ae9f5e924b84ba92596c5cdcc8d30a2e9104f9589"

    bot = Bot(token=token)

    for bp in load_blueprints_from_package("blueprints"):
        bp.load(bot)

    print("Ready...")
    bot.run_forever()


if __name__ == "__main__":
    main(os.environ.get("TOKEN"))
