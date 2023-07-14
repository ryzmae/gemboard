from src import Gemboard

client = Gemboard()

if __name__ == "__main__":
    client.loadCommands(
        dir="src/commands",
        sub=False
    )

    client.run()