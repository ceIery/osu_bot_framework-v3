def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# contains common command responses
class CommonCommands:
    def __init__(self, bot, channel):
        self.bot = bot
        self.channel = channel

    def config_link(self, message):
        self.channel.send_message("The configuration of the game room and available commands can be viewed [" + self.channel.get_config_link() + " here]")

    def randmap(self, message):
        command = message["content"].split(" ", 1)[0]
        if self.channel.get_formatted_host() == message["username"] or message["username"] in self.channel.get_formatted_referees():
            query = message["content"].replace(command, "", 1).strip()
            if query == "":
                self.channel.send_message("Searching for beatmap...")
            else:
                self.channel.send_message("Searching for '" + query + "'...")

            beatmap = self.bot.chimu.fetch_random_beatmap(self.channel, query=query)
            if beatmap:
                self.channel.change_beatmap(beatmap["BeatmapId"])
            else:
                self.channel.send_message("No beatmaps found!")
        else:
            self.channel.send_message("This command is only available to the host or referees.")

    def altlink(self, message):
        self.channel.send_message("An alternate download link is available [" + self.bot.chimu.fetch_download_link(self.channel.get_beatmap()["id"]) + " here]")

    def ar_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_ar_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")

    def od_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_od_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")

    def hp_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_hp_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def cs_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_cs_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def bpm_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_bpm_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def diff_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_diff_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def length_range(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 2:
                if all([is_number(arg) for arg in args]):
                    self.channel.set_length_range((float(args[0]), float(args[1])))
                else:
                    self.channel.send_message(message["username"] + " you can only send numbers with this command.")
                    return
            else:
                self.channel.send_message(message["username"] + " you must send 2 arguments with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def map_status(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if args:
                self.channel.set_map_status(args)
            else:
                self.channel.set_map_status("any")
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def mods(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if args:
                self.channel.set_mods(args)
            else:
                self.channel.set_mods("any")
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def scoring_type(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 1:
                self.channel.set_scoring_type(args[0])
            elif not args:
                self.channel.set_scoring_type("any")
            else:
                self.channel.send_message(message["username"] + " you must send 1 argument with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def team_type(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 1:
                self.channel.set_team_type(args[0])
            elif not args:
                self.channel.set_team_type("any")
            else:
                self.channel.send_message(message["username"] + " you must send 1 argument with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
            
    def game_mode(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 1:
                self.channel.set_game_mode(args[0])
            elif not args:
                self.channel.set_game_mode("any")
            else:
                self.channel.send_message(message["username"] + " you must send 1 argument with this command.")
                return
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")

    def welcome_message(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            msg = message["content"].replace(command, "", 1).strip()
            if msg:
                self.channel.set_welcome_message(msg)
            else:
                self.channel.set_welcome_message("")
            self.channel.send_message("Command '" + command + "' executed successfully")
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")

    def add_broadcast(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) > 1:
                if is_number(args[0]):
                   id = self.channel.add_broadcast(" ".join(args[1:]), args[0])
                   self.channel.send_message("Broadcast id: " + str(id) + " started")
            else:
                self.channel.send_message(message["username"] + " you must send a time in seconds and a message to broadcast.")
                return
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")
    
    def del_broadcast(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 1:
                if self.bot.has_broadcast_id(args[0]):
                    self.bot.del_broadcast(args[0])
                else:
                    self.channel.send_message(message["username"] + " broadcast id not recognised.")
                    return
                self.channel.send_message("Broadcast id: " + args[0] + " stopped")
            else:
                self.channel.send_message(message["username"] + " you must send 1 argument with this command.")
                return
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")

    def implement_logic_profile(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            command = message["content"].split(" ", 1)[0]
            args = message["content"].replace(command, "", 1).strip().split(" ")
            if len(args) == 1:
                if args[0] in self.bot.get_logic_profiles():
                    self.channel.implement_logic_profile(args[0])
                else:
                    self.channel.send_message(message["username"] + " this logic profile does not exist.")
                    return
                self.channel.send_message("Command '" + command + "' executed successfully")
            else:
                self.channel.send_message(message["username"] + " you must send 1 argument with this command.")
                return
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")

    def get_logic_profiles(self, message):
        if message["username"] in self.channel.get_formatted_referees():
            self.channel.send_message("Available logic profiles: " + ", ".join(self.bot.get_logic_profiles().keys()))
        else:
            self.channel.send_message("Sorry " + message["username"] + " that command is only for referees!")