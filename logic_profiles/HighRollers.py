import random
import time


class HighRollers:
    def __init__(self, bot, channel):
        self.bot = bot
        self.channel = channel

        self.roll_time = 30
        self.rolls = {}
        self.rolls_in_progress = False

    def on_join(self, username):
        if self.channel.get_users() == [username]:
            self.rolls = {}
            self.rolls_in_progress = False
            self.channel.set_host(username)

    def on_part(self, username):
        if username in self.rolls:
            del self.rolls[username]

    def on_match_finish(self):
        self.rolls = {}
        self.rolls_in_progress = True

        self.channel.send_message("You have " + str(self.roll_time) + " seconds to !roll for host...")
        for i in reversed(range(self.roll_time)):
            time.sleep(1)
            if i == 9:
                self.channel.send_message("rolling concludes in 10 seconds...")
            if i < 5:
                self.channel.send_message("rolling concludes in " + str(i + 1))
            if not self.channel.has_users():
                self.rolls_in_progress = False
                return
            if len(self.rolls) == len(self.channel.get_users()):
                break

        self.rolls_in_progress = False
        if self.rolls:
            username = max(self.rolls, key=self.rolls.get)
            self.channel.send_message(username + " took the host with " + str(self.rolls[username]) + " points rolled!")
            self.channel.set_host(username)
        else:
            self.channel.send_message("Nobody rolled! Picking random host...")
            self.channel.set_host(random.choice(self.channel.get_users()))

    def on_message(self, message):
        if message["username"] == "BanchoBot" and " rolls " in message["content"] and self.rolls_in_progress:
            user = message["content"][:message["content"].find("rolls")].strip()
            if user not in self.rolls:
                points = int(message["content"].replace(user + " rolls ", "").split(" ", 1)[0])
                if points <= 100:
                    self.rolls[user] = points
                else:
                    self.channel.send_message(user + " you may only type '!roll'")
            else:
                self.channel.send_message(user + " only your first !roll counts!")