import os


def main(token):
    from vkbottle import Bot, load_blueprints_from_package

    # token = ""

    bot = Bot(token=token)

    for bp in load_blueprints_from_package("blueprints"):
        bp.load(bot)

    print("Ready...")
    bot.run_forever()


if __name__ == "__main__":
    main(os.environ.get("TOKEN"))
