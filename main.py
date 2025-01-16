import asyncio
import logging
import random
import socket
import requests
import json
import sys
from typing import Union
from highrise import (
    AnchorPosition,
    BaseBot,
    Position,
    User,
)
from highrise.models import (
    CurrencyItem,
    SessionMetadata,
)
from keep_alive import keep_alive

# Call the keep_alive function to start the Flask server
keep_alive()
import requests
url = 'https://pocket.mizhabansar.repl.co'

response = requests.get(url, allow_redirects=False)


class Bot(BaseBot):
    def __init__(self):
        super().__init__()
        self.tipped_users = set()
        self.user_bags = {}
        self.encountered_pokemon = {}
        self.caught_pokemon = {}
        self.leaderboard = {}
        self.is_paused = False  # Initialize the paused flag
        self.pause_duration = 300  # 5 minutes in seconds
        self.load_data()

    async def handle_network_errors(self, max_retries: int, retry_delay: int) -> None:
        """
        Handle network errors and retries for bot operations.
        """
        for retry_count in range(max_retries):
            try:
                # Your bot logic goes here
                # Example: await some_function()

                # Sleep or do other tasks
                await asyncio.sleep(1)
            except (Exception, requests.exceptions.RequestException, socket.error) as e:
                print("Error: ", e)
                logging.error(f"Network error: {e}")

                # Retry the operation
                print(f"Retrying {retry_count + 1}/{max_retries}...")
                await asyncio.sleep(retry_delay)
                continue
            except Exception as e:
                print("Error: ", e)
                logging.error(f"Error: {e}")
                # Handle other exceptions here as needed

    async def on_start(self, session_metadata: SessionMetadata) -> None:
        max_retries = 3  # Maximum number of retry attempts
        retry_delay = 5  # Initial retry delay in seconds

        # Define the list of positions
        self.positions = [
            Position(x=9.5, y=0.25, z=18.5, facing='BackRight'),
            Position(x=8.0, y=0.5, z=23.5, facing='FrontRight'),
            Position(x=1.0, y=0.0, z=11.0, facing='FrontRight'),
            Position(x=10.5, y=0.25, z=11.0, facing='FrontRight'),
            Position(x=0.5, y=0.5, z=3.5, facing='BackLeft'),
            Position(x=10.5, y=0.25, z=11.5, facing='FrontRight'),
            Position(x=1.0, y=0.0, z=24.5, facing='FrontRight'),
            Position(x=14.5, y=5.25, z=28.5, facing='FrontRight'),
            Position(x=14.5, y=5.25, z=20.5, facing='FrontLeft'),
            Position(x=14.5, y=5.75, z=13.5, facing='FrontRight'),
            Position(x=14.5, y=5.75, z=7.5, facing='FrontRight'),
            Position(x=12.5, y=6.75, z=4.5, facing='FrontRight'),
            Position(x=0.5, y=5.800000190734863, z=4.5, facing='FrontRight'),
            AnchorPosition(entity_id='6504a46200000000000000c7', anchor_ix=0),
            # Add more positions as needed
        ]

        for retry_count in range(max_retries):
            try:
                print("\033[1;96mBOT IN THE ROOM\033[0m")
                await self.highrise.chat("Sorry, my coder was coding me")
                await self.highrise.chat("NVM, I am back ONLINE")
                while True:  # Add a loop for continuous movement
                    # Randomly select a position from the list
                    selected_position = random.choice(self.positions)

                    await self.highrise.tg.create_task(
                        self.highrise.walk_to(selected_position)
                    )

                    await asyncio.sleep(20)  # Wait for 15 seconds before moving again
                    
                    
                break  # If successful, exit the loop
            except Exception:
                print("\033[1;91mReconnection failed. Retrying in {retry_delay} seconds...\033[0m")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff

                if retry_count == max_retries - 1:
                    print("\033[1;91mMax retries reached. Unable to connect.\033[0m")



    
    
    async def on_user_join(self, user: User, position: Union[Position, AnchorPosition]) -> None:
       while True:
            try:
                print(f"\033[1;32m {user.username} Joined the Room. \033[0m")
                await self.highrise.chat (f"Wᴇʟᴄᴏᴍᴇ,@{user.username} PᴏᴋÉᴍᴏɴ ᴛʀᴀɪɴᴇʀ! ʏᴏᴜʀ ᴄᴏᴍᴍᴀɴᴅꜱ: \n Cᴀᴛᴄʜ - ᴄᴀᴛᴄʜ ᴘᴏᴋÉᴍᴏɴ\n Bᴀɢ - ᴄʜᴇᴄᴋ ᴘᴏᴋÉʙᴀʟʟꜱ \n Sᴄᴏʀᴇ - ᴠɪᴇᴡ ʏᴏᴜʀ ꜱᴄᴏʀᴇ \n Bᴏᴀʀᴅ - ᴄʜᴇᴄᴋ ᴛʜᴇ ʟᴇᴀᴅᴇʀʙᴏᴀʀᴅ\n Pᴏᴋᴇʟɪꜱᴛ - ꜱᴇᴇ ʏᴏᴜʀ ʟᴀꜱᴛ 20 ᴄᴀᴛᴄʜᴇꜱ\n Pᴏᴋᴇᴅᴇx - ᴠɪᴇᴡ ᴀʟʟ ʏᴏᴜʀ ᴘᴏᴋÉᴍᴏɴ.")
                await self.highrise.chat("Nᴇᴇᴅ ᴍᴏʀᴇ ᴘᴏᴋÉʙᴀʟʟꜱ? ᴛɪᴘ ᴍᴇ.\n Sᴛᴀʏ ᴛᴜɴᴇᴅ ꜰᴏʀ ᴘᴏᴋÉᴍᴏɴ ᴛᴏᴜʀɴᴀᴍᴇɴᴛꜱ!")
                await self.highrise.send_emote(random.choice(["idle-dance-swinging","dance-breakdance","dance-floss","emote-frollicking", "emote-ghost-idle","emote-graceful","emote-headball","emote-hero","emote-monster_fail","dance-robotic","dance-spiritual", "sit-idle-cute"]))
                break 
            except Exception as e:
                print(f"\033[1;91m Joining failed. Exception: {str(e)}\033[0m")
                await asyncio.sleep(5)
                break
                
                
    async def on_chat(self, user: User, message: str) -> None:
        try:
            print(f"\033[1;91m {user.username} said: {message} \033[0m")
            if message == 'Play' or message == 'play':
                    await self.highrise.chat(f'{user.username} has entered the Arena!')
                    await self.highrise.teleport(user.id, Position(16.5, 5.75, 14.5))
            
            elif message == 'Catch' or message == 'catch':
                if self.is_paused:
                    await self.highrise.send_whisper(user.id, "The bot is currently paused. It will resume shortly.")
                elif user.username in self.user_bags and self.user_bags[user.username] > 0:
                    if user.username in self.encountered_pokemon:
                        pokemon_name = self.encountered_pokemon[user.username]
                        if pokemon_name in ['Venusaur','Charizard','Blastoise','Butterfree','Beedrill','Pidgeot','Raticate','Fearow','Arbok','Raichu','Sandslash','Nidoqueen','Nidoking','Clefable','Ninetales','Wigglytuff','Golbat','Vileplume','Parasect','Venomoth','Dugtrio','Persian','Golduck','Primeape','Arcanine','Poliwrath','Machamp','Alakazam','Victreebel','Tentacruel','Golem','Rapidash','Slowbro','Magneton','Dodrio','Dewgong','Muk','Cloyster','Gengar','Kingler','Electrode','Exeggutor','Marowak','Weezing','Seaking','Starmie','Gyarados','Vaporeon','Jolteon','Flareon','Omastar','Kabutops','Aerodactyl','Snorlax','Dragonite'] :
                            if random.random() <= 0.3:
                                if user.username in self.caught_pokemon:
                                    self.caught_pokemon[user.username].append(pokemon_name)
                                else:
                                    self.caught_pokemon[user.username] = [pokemon_name]
                                points = self.get_pokemon_points(pokemon_name)
                                await self.highrise.send_whisper(user.id, f"Congratulations! You caught {pokemon_name} (+{points} points)!")
                                self.user_bags[user.username] -= 1
                                del self.encountered_pokemon[user.username]
                                self.update_leaderboard(user.username, points)
                                self.save_caught_pokemon_data()
                                self.save_leaderboard_data()
                                await self.highrise.send_whisper(user.id, "Search for other Pokémon in different locations!")
                            else:
                                await self.highrise.send_whisper(user.id, f"Oh no! {pokemon_name} broke free of the Pokéball. Try to Catch again.")
                                self.user_bags[user.username] -= 1

                        elif pokemon_name in ['Articuno','Zapdos','Moltres','Mewtwo','Mew'] :
                            if random.random() <= 0.01:
                                if user.username in self.caught_pokemon:
                                    self.caught_pokemon[user.username].append(pokemon_name)
                                else:
                                    self.caught_pokemon[user.username] = [pokemon_name]
                                points = self.get_pokemon_points(pokemon_name)
                                await self.highrise.send_whisper(user.id, f"Congratulations! You caught {pokemon_name} (+{points} points)!")
                                self.user_bags[user.username] -= 1
                                del self.encountered_pokemon[user.username]
                                self.update_leaderboard(user.username, points)
                                self.save_caught_pokemon_data()
                                self.save_leaderboard_data()
                                await self.highrise.send_whisper(user.id, "Search for other Pokémon in different locations!")
                            else:
                                await self.highrise.send_whisper(user.id, f"Oh no! {pokemon_name} broke free of the Pokéball. Try to Catch again.")
                                self.user_bags[user.username] -= 1

                        else:
                            # For other Pokémon, use the default catch rate (50% in this case)
                            if random.random() <= 0.8:
                                if user.username in self.caught_pokemon:
                                    self.caught_pokemon[user.username].append(pokemon_name)
                                else:
                                    self.caught_pokemon[user.username] = [pokemon_name]
                                points = self.get_pokemon_points(pokemon_name)
                                await self.highrise.send_whisper(user.id, f"Congratulations! You caught {pokemon_name} (+{points} points)!")
                                self.user_bags[user.username] -= 1
                                del self.encountered_pokemon[user.username]
                                self.update_leaderboard(user.username, points)
                                self.save_caught_pokemon_data()
                                self.save_leaderboard_data()
                                await self.highrise.send_whisper(user.id, "Search for other Pokémon in different locations!")
                            else:
                                await self.highrise.send_whisper(user.id, f"Oh no! {pokemon_name} broke free of the Pokéball. Try to Catch again.")
                                self.user_bags[user.username] -= 1
                    else:
                        await self.highrise.send_whisper(user.id, "No Pokémon encountered. Move around to find wild Pokémon.")
                else:
                    await self.highrise.send_whisper(user.id, "You don't have any Pokéballs. Tip Gottacatchemall to buy:\n"
                                  "1 Pokéball = 1g\n"
                                  "5 Pokéball = 5g\n"
                                  "10 Pokéballs = 10g\n"
                                  "50 Pokéballs = 50g\n"
                                  "100 Pokéballs = 100g\n"
                                  "500 Pokéballs = 500g\n"
                                  "1000 Pokéballs = 1000g\n"
                                  "5000 Pokéballs = 5000g\n"
                                  "10000 Pokéballs = 10000g\n"
                                  )

            elif message.startswith('Free') or message.startswith('free') :
                if user.username == 'ZUIMZ'or user.username == "MetaMiz":
                    target_username = message.split(' ')[1]
                    if target_username.startswith('@'):
                        target_username = target_username[1:]  # Remove the '@' symbol
                        if target_username in self.user_bags:
                            self.user_bags[target_username] += 5
                        else:
                            self.user_bags[target_username] = 5
                        await self.highrise.send_whisper(user.id, f"You have given 5 free Pokéballs to {target_username}.")
                        self.save_pokeballs_data()  # Save pokeballs data to JSON
                    else:
                        await self.highrise.send_whisper(user.id, "Please mention a valid user with '@username'.")
                else:
                    await self.highrise.send_whisper(user.id, "You don't have permission to use this command.")

            elif message == 'Bag' or message == 'bag':
                if user.username in self.user_bags:
                    await self.highrise.send_whisper(user.id, f"You have {self.user_bags[user.username]} Pokéballs.")
                else:
                    await self.highrise.send_whisper(user.id, "You don't have any Pokéballs.")

            elif message == 'Pokelist' or message == 'pokelist':
                if user.username in self.caught_pokemon:
                    caught_pokemons = self.caught_pokemon[user.username]
                    last_three_pokemons = caught_pokemons[-20:]  # Get the last three caught Pokémon
                    pokemons = ', '.join(last_three_pokemons)
                    await self.highrise.send_whisper(user.id, f"Your last 20 Pokémon: {pokemons}")
                else:
                    await self.highrise.send_whisper(user.id, "You haven't caught any Pokémon yet.")

            elif message == 'Board' or message == 'board':
                self.load_leaderboard_data()  # Load leaderboard data from JSON
                leaderboard_message = "Leaderboard:\n"
                for rank, entry in enumerate(self.leaderboard[:5], start=1):
                    leaderboard_message += f"{rank}. {entry['username']}: {entry['points']} points\n"
                await self.highrise.chat(leaderboard_message)

            elif message == 'Score' or message == 'score':
                self.load_leaderboard_data()  # Load leaderboard data from JSON
                
                user_score = None
                for entry in self.leaderboard:
                    if entry['username'] == user.username:
                        user_score = entry['points']
                        break
                
                if user_score is not None:
                    score_message = f"Your score: {user_score} points"
                else:
                    score_message = "You don't have a score yet"
                
                await self.highrise.send_whisper(user.id, score_message)

            elif message == 'Pokedex' or message == 'pokedex':
                if user.username in self.caught_pokemon:
                    caught_pokemons = self.caught_pokemon[user.username]
                    unique_pokemons = list(set(caught_pokemons))
                    chunk_size = 10  
                    page = 1

                    while (page - 1) * chunk_size < len(unique_pokemons):
                        start_index = (page - 1) * chunk_size
                        end_index = min(page * chunk_size, len(unique_pokemons))
                        pokedex_chunk = unique_pokemons[start_index:end_index]

                        pokedex_message = f"Page {page} of your Pokédex:\n"
                        pokedex_message += ", ".join(pokedex_chunk)

                        await self.highrise.send_whisper(user.id, pokedex_message)

                        page += 1

            elif message == 'Stop' or message == 'stop':
                if user.username == 'ZUIMZ': 
                    await self.highrise.chat("Stopping the bot.")
                    sys.exit()
                    
        except Exception as e:
            print(f"\033[1;31m Chat failed. Error: {str(e)}\033[0m")
            await asyncio.sleep(5)

            
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem) -> None:
      try:
        print("\033[1;93m [TIP] {} tipped {} {}g\033[0m".format(sender.username, receiver.username, tip.amount))
        if receiver.username == 'ProfessorOak':
            if tip.amount == 1:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 1
                else:
                    self.user_bags[sender.username] = 1
                await self.highrise.send_whisper(sender.id, "You have purchased a 1 Pokéball.")
                self.save_pokeballs_data()  # Save pokeballs data to JSON
            elif tip.amount == 5:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 5
                else:
                    self.user_bags[sender.username] = 5
                await self.highrise.send_whisper(sender.id, "You have purchased 5 Pokéballs.")
                # Save data to JSON
                self.save_data()
                
            elif tip.amount == 10:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 10
                else:
                    self.user_bags[sender.username] = 10
                await self.highrise.send_whisper(sender.id, "You have purchased 10 Pokéballs.")
                # Save data to JSON
                self.save_data()

            elif tip.amount == 50:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 50
                else:
                    self.user_bags[sender.username] = 50
                await self.highrise.send_whisper(sender.id, "You have purchased 50 Pokéballs.")
                # Save data to JSON
                self.save_data()

            elif tip.amount == 100:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 100
                else:
                    self.user_bags[sender.username] = 100
                await self.highrise.send_whisper(sender.id, "You have purchased 100 Pokéballs.")
                # Save data to JSON
                self.save_data()

            elif tip.amount == 500:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 500
                else:
                    self.user_bags[sender.username] = 500
                await self.highrise.send_whisper(sender.id, "You have purchased 500 Pokéballs.")
                # Save data to JSON
                self.save_data()
                
            elif tip.amount == 1000:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 1000
                else:
                    self.user_bags[sender.username] = 1000
                await self.highrise.send_whisper(sender.id, "You have purchased 1000 Pokéballs.")
                # Save data to JSON
                self.save_data()

            elif tip.amount == 5000:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 5000
                else:
                    self.user_bags[sender.username] = 5000
                await self.highrise.send_whisper(sender.id, "You have purchased 5000 Pokéballs.")
                # Save data to JSON
                self.save_data()
                
            elif tip.amount == 10000:
                if sender.username in self.user_bags:
                    self.user_bags[sender.username] += 10000
                else:
                    self.user_bags[sender.username] = 10000
                await self.highrise.send_whisper(sender.id, "You have purchased 10000 Pokéballs.")
                # Save data to JSON
                self.save_data()
        
      except Exception:
                print("\033[1;91m Tipping failed. Retrying in 5 seconds...\033[0m")
                await asyncio.sleep(5)

    async def on_whisper(self, user: User, message: str) -> None:
       while True:
            try:
                print(f"\033[1;92m {user.username} whispered: {message}\033[0m")
                if "legendary" in message.lower():
                    try:
                        await self.highrise.teleport(f"{user.id}", Position(0.5, 10.5,0.5))
                    except Exception as e:
                        print("error 3:", e)
                    break 
              
            except Exception:
                print("\033[1;91m Whispering failed. Retrying in 5 seconds...\033[0m")
                await asyncio.sleep(5)
                break
   
    async def on_user_move(self, user: User, pos: Position) -> None:
        while True:
            try:
                if user.username in ["MetaMiz", "ZUIMZ"]:
                    print(f"\033[1;30m {user.username} moved to {pos},\033[0m")

                if hasattr(pos, 'x'):
                    if ((pos.x <= 17.5 and pos.x >= 0.5) and (pos.y == 0.5) and (pos.z <= 7.5 and pos.z >= 0.5)):
                        pokemon_name = self.safari()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 0.5) and (pos.y == 0.25) and (pos.z <= 7.5 and pos.z >= 0.5)):
                        pokemon_name = self.normal()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 1.0) and (pos.y == 0.0) and (pos.z <= 17.5 and pos.z >= 8.5)):
                        pokemon_name = self.water()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 1.0) and (pos.y >= 0.0 and pos.y <= 0.5) and (pos.z <= 17.5 and pos.z >= 8.5)):
                        pokemon_name = self.normal()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 0.5) and (pos.y == 0.25) and (pos.z <= 19.5 and pos.z >= 18.5)):
                        pokemon_name = self.safari()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 0.5) and (pos.y == 0.0) and (pos.z <= 29.5 and pos.z >= 20.5)):
                        pokemon_name = self.water()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 0.5) and (pos.y >= 0.25 and pos.y <= 0.5) and (pos.z <= 29.5 and pos.z >= 20.5)):
                        pokemon_name = self.ice()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 14.5) and (pos.y == 5.25) and (pos.z <= 29.5 and pos.z >= 22.5)):
                        pokemon_name = self.sky()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 14.5) and (pos.y >= 5.25 and pos.y <= 5.75) and (pos.z <= 21.5 and pos.z >= 14.5)):
                        pokemon_name = self.ivy()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 14.5) and (pos.y >= 5.75 and pos.y <= 6.0) and (pos.z <= 13.5 and pos.z >= 5.5)):
                        pokemon_name = self.darkforest()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 17.5 and pos.x >= 8.5) and (pos.y >= 6.75 and pos.y <= 7.0) and (pos.z <= 4.5 and pos.z >= 0.5)):
                        pokemon_name = self.savanah()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 7.5 and pos.x >= 0.5) and (pos.y >= 5.75 and pos.y <= 6.75) and (pos.z <= 4.5 and pos.z >= 0.5)):
                        pokemon_name = self.rocky()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    elif ((pos.x <= 2.5 and pos.x >= 0.5) and (pos.y == 10.5) and (pos.z <= 2.5 and pos.z >= 0.5)):
                        pokemon_name = self.legendary()
                        self.encountered_pokemon[user.username] = pokemon_name
                        await self.highrise.send_whisper(user.id, f"You have encountered a wild {pokemon_name}!")

                    else:
                        await self.highrise.send_whisper(user.id, "No Pokémon encountered.")
                else:
                    await self.highrise.send_whisper(user.id, "No Pokémon encountered.")

                break
            except Exception as e:
                print("\033[1;31m Moving error:", e, "\033[0m")
                break
            
    def kanto(self) -> str:
        pokemon_list=['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Sandshrew','Sandslash','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Clefairy','Clefable','Vulpix','Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Diglett','Dugtrio','Meowth','Persian','Psyduck','Golduck','Mankey','Primeape','Growlithe','Arcanine','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Geodude','Graveler','Golem','Ponyta','Rapidash','Slowpoke','Slowbro','Magnemite','Magneton','Farfetch\'d','Doduo','Dodrio','Seel','Dewgong','Grimer','Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Tangela','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr.Mime','Scyther','Jynx','Electabuzz','Magmar','Pinsir','Tauros','Magikarp','Gyarados','Lapras','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew']
        return random.choice(pokemon_list)

    def johto(self) -> str:
        johto_pokemon_list = [
        'Chikorita','Bayleef','Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion',
        'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot',
        'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou',
        'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu',
        'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill',
        'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern',
        'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow',
        'Slowking', 'Misdreavous', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco',
        'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull',
        'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa',
        'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid',
        'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom',
        'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue',
        'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou',
        'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-Oh',
        'Celebi'
        ]
        return random.choice(johto_pokemon_list)

    def hoenn(self) -> str:
        hoenn_pokemon_list = [
        'Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken',
        'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon',
        'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox',
        'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow',
        'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit',
        'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking',
        'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita',
        'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile',
        'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric',
        'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot',
        'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal',
        'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea',
        'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock',
        'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep',
        'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Castform', 'Kecleon',
        'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol',
        'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl',
        'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence',
        'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias',
        'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys'
        ]
        return random.choice(hoenn_pokemon_list)
    
    def sinnoh(self) -> str:
        sinnoh_pokemon_list = [
        'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape',
        'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor',
        'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray',
        'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon',
        'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel',
        'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom',
        'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow',
        'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor',
        'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible',
        'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas',
        'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine',
        'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile',
        'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar',
        'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine',
        'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom',
        'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas',
        'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus'
    ]
        return random.choice(sinnoh_pokemon_list)

    def unova(self) -> str:
        unova_pokemon_list = [
        'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar',
        'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Lillipup',
        'Herdier', 'Stoutland', 'Purrloin', 'Liepard', 'Pansage', 'Simisage',
        'Pansear', 'Simisear', 'Panpour', 'Simipour', 'Munna', 'Musharna',
        'Pidove', 'Tranquill', 'Unfezant', 'Blitzle', 'Zebstrika', 'Roggenrola',
        'Boldore', 'Gigalith', 'Woobat', 'Swoobat', 'Drilbur', 'Excadrill',
        'Audino', 'Timburr', 'Gurdurr', 'Conkeldurr', 'Tympole', 'Palpitoad',
        'Seismitoad', 'Throh', 'Sawk', 'Sewaddle', 'Swadloon', 'Leavanny',
        'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott',
        'Petilil', 'Lilligant', 'Basculin', 'Sandile', 'Krokorok', 'Krookodile',
        'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Scraggy',
        'Scrafty', 'Sigilyph', 'Yamask', 'Cofagrigus', 'Tirtouga', 'Carracosta',
        'Archen', 'Archeops', 'Trubbish', 'Garbodor', 'Zorua', 'Zoroark', 'Minccino',
        'Cinccino', 'Gothita', 'Gothorita', 'Gothitelle', 'Solosis', 'Duosion',
        'Reuniclus', 'Ducklett', 'Swanna', 'Vanillite', 'Vanillish', 'Vanilluxe',
        'Deerling', 'Sawsbuck', 'Emolga', 'Karrablast', 'Escavalier', 'Foongus',
        'Amoonguss', 'Frillish', 'Jellicent', 'Alomomola', 'Joltik', 'Galvantula',
        'Ferroseed', 'Ferrothorn', 'Klink', 'Klang', 'Klinklang', 'Tynamo', 'Eelektrik',
        'Eelektross', 'Elgyem', 'Beheeyem', 'Litwick', 'Lampent', 'Chandelure',
        'Axew', 'Fraxure', 'Haxorus', 'Cubchoo', 'Beartic', 'Cryogonal', 'Shelmet',
        'Accelgor', 'Stunfisk', 'Mienfoo', 'Mienshao', 'Druddigon', 'Golett',
        'Golurk', 'Pawniard', 'Bisharp', 'Bouffalant', 'Rufflet', 'Braviary',
        'Vullaby', 'Mandibuzz', 'Heatmor', 'Durant', 'Deino', 'Zweilous', 'Hydreigon',
        'Larvesta', 'Volcarona', 'Cobalion', 'Terrakion', 'Virizion', 'Tornadus',
        'Thundurus', 'Reshiram', 'Zekrom', 'Landorus', 'Kyurem', 'Keldeo',
        'Meloetta', 'Genesect'
        ]
        return random.choice(unova_pokemon_list)

    def savanah(self) -> str:
        pokemon_list=['Charmander','Charmeleon','Ratata','Raticate','Sandshrew','Sandslash','Growlithe','Arcanine','Charizard','Magmar','Ponyta','Rapidash']
        return random.choice(pokemon_list)

    def rocky(self) -> str:
        pokemon_list=['Geodude','Graveler','Golem','Raticate','Sandshrew','Sandslash','Onix','Rhyhorn','Rhydon','Kabuto','Omanyte','Aerodactyl']
        return random.choice(pokemon_list)

    def darkforest(self) -> str:
        pokemon_list=['Bulbasaur','Ivysaur','Venusaur','Zubat','Golbat','Oddish','Gloom','Vileplume','Paras','Parasect','Venonat','Venomoth','Gastly','Haunter','Gengar','Pinsir']
        return random.choice(pokemon_list)

    def ivy(self) -> str:
        pokemon_list=['Bulbasaur','Ivysaur','Venusaur','Zubat','Golbat','Oddish','Gloom','Vileplume','Venonat','Venomoth','Nidoran♀','Nidorina','Nidoqueen','Nidoran♂','Nidorino','Nidoking','Bellsprout','Weepinbell','Victreebel','Koffing','Weezing']
        return random.choice(pokemon_list)

    def sky(self) -> str:
        pokemon_list=['Butterfree','Beedrill','Pidgey','Pidgeotto','Pidgeot','Zubat','Golbat','Venomoth','Aerodactyl','Charizard','Farfetch\'d','Doduo','Dodrio','Dratini','Dragonair','Dragonite',]
        return random.choice(pokemon_list)

    def ice(self) -> str:
        pokemon_list=['Seel','Dewgong','Shellder','Cloyster','Jynx',]
        return random.choice(pokemon_list)

    def water(self) -> str:
        pokemon_list=['Squirtle','Wartortle','Blastoise','Poliwag','Poliwhirl','Poliwrath','Seel','Dewgong','Shellder','Cloyster','Jynx','Tentacool','Tentacruel','Slowpoke','Slowbro','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Krabby','Kingler','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Magikarp','Gyarados','Lapras','Psyduck','Golduck',]
        return random.choice(pokemon_list)

    def normal(self) -> str:
        pokemon_list=['Caterpie','Metapod','Butterfree','Weedle','Kakuna','Beedrill','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Mankey','Primeape']
        return random.choice(pokemon_list)

    def safari(self) -> str:
        pokemon_list=['Clefairy','Clefable','Jigglypuff','Wigglytuff','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Magnemite','Magneton','Farfetch\'d','Doduo','Dodrio','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Exeggcute','Exeggutor','Cubone','Marowak','Hitmonlee','Hitmonchan','Lickitung','Mr.Mime','Scyther','Pinsir','Tauros','Ditto','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Snorlax','Dratini','Dragonair','Dragonite','Chansey','Tangela','Kangaskhan',]
        return random.choice(pokemon_list)

    def legendary(self) -> str:
        pokemon_list=['Articuno','Zapdos','Moltres','Mewtwo','Mew']
        return random.choice(pokemon_list)

    def final(self) -> str:
        pokemon_list=['Venusaur','Charizard','Blastoise','Butterfree','Beedrill','Pidgeot','Raticate','Fearow','Arbok','Raichu','Sandslash','Nidoqueen','Nidoking','Clefable','Ninetales','Wigglytuff','Golbat','Vileplume','Parasect','Venomoth','Dugtrio','Persian','Golduck','Primeape','Arcanine','Poliwrath','Machamp','Alakazam','Victreebel','Tentacruel','Golem','Rapidash','Slowbro','Magneton','Dodrio','Dewgong','Muk','Cloyster','Gengar','Kingler','Electrode','Exeggutor','Marowak','Weezing','Seaking','Starmie','Gyarados','Vaporeon','Jolteon','Flareon','Omastar','Kabutops','Aerodactyl','Snorlax','Dragonite']
        return random.choice(pokemon_list)

    def get_pokemon_points(self, pokemon_name: str) -> int:
        points = {
            'Bulbasaur': 10,
            'Ivysaur': 20,
            'Venusaur': 30,
            'Charmander' : 10,
            'Charmeleon': 20,
            'Charizard': 30,
            'Squirtle': 10,
            'Wartortle': 20,
            'Blastoise': 30,
            'Caterpie': 5,
            'Metapod': 10,
            'Butterfree': 15,
            'Weedle': 5,
            'Kakuna': 10,
            'Beedrill': 15,
            'Pidgey' : 5,
            'Pidgeotto': 10,
            'Pidgeot': 20,
            'Rattata': 5,
            'Raticate': 15,
            'Spearow': 5,
            'Fearow': 15,
            'Ekans' : 5,
            'Arbok': 15,
            'Pikachu': 5,
            'Raichu': 25,
            'Sandshrew': 5,
            'Sandslash': 15,
            'Nidoran♀': 5,
            'Nidorina': 15,
            'Nidoqueen': 25,
            'Nidoran♂': 5,
            'Nidorino': 15,
            'Nidoking': 25,
            'Clefairy': 5,
            'Clefable': 25,
            'Vulpix': 5,
            'Ninetales': 25,
            'Jigglypuff': 5,
            'Wigglytuff': 20,
            'Zubat': 5,
            'Golbat': 15,
            'Oddish': 5,
            'Gloom': 15,
            'Vileplume': 25,
            'Bellossom' : 25,
            'Paras': 5,
            'Parasect': 15,
            'Venonat': 5,
            'Venomoth': 15,
            'Diglett': 5,
            'Dugtrio': 15,
            'Meowth': 5,
            'Persian': 15,
            'Psyduck': 5,
            'Golduck': 15,
            'Mankey' : 5,
            'Primeape': 15,
            'Growlithe': 5,
            'Arcanine': 25,
            'Poliwag': 5,
            'Poliwhirl': 15,
            'Poliwrath': 25,
            'Abra': 5,
            'Kadabra': 15,
            'Alakazam': 25,
            'Machop': 10,
            'Machoke': 15,
            'Machamp': 25,
            'Bellsprout': 5,
            'Weepinbell': 15,
            'Victreebel': 20,
            'Tentacool': 5,
            'Tentacruel': 20,
            'Geodude': 5,
            'Graveler': 15,
            'Golem': 25,
            'Ponyta': 5,
            'Rapidash': 15,
            'Slowpoke': 5,
            'Slowbro': 20,
            'Magnemite': 5,
            'Magneton': 15,
            'Farfetch\'d': 5,
            'Doduo': 5,
            'Dodrio': 15,
            'Seel': 5,
            'Dewgong': 20,
            'Grimer': 5,
            'Muk': 15,
            'Shellder': 5,
            'Cloyster': 20,
            'Gastly': 5,
            'Haunter': 15,
            'Gengar': 25,
            'Onix': 5,
            'Drowzee': 5,
            'Hypno': 15,
            'Krabby': 5,
            'Kingler': 20,
            'Voltorb': 5,
            'Electrode': 15,
            'Exeggcute': 5,
            'Exeggutor': 20,
            'Cubone': 5,
            'Marowak': 15,
            'Hitmonlee': 20,
            'Hitmonchan': 20,
            'Lickitung': 20,
            'Koffing': 5,
            'Weezing': 15,
            'Rhyhorn': 5,
            'Rhydon': 15,
            'Chansey': 20,
            'Tangela': 20,
            'Kangaskhan': 20,
            'Horsea': 5,
            'Seadra': 15,
            'Goldeen': 5,
            'Seaking': 15,
            'Staryu' : 5,
            'Starmie': 15,
            'Mr. Mime': 20,
            'Scyther': 15,
            'Jynx': 20,
            'Electabuzz': 20,
            'Magmar': 20,
            'Pinsir': 20,
            'Tauros': 20,
            'Magikarp': 5,
            'Gyarados': 25,
            'Lapras': 15,
            'Ditto': 20,
            'Eevee': 5,
            'Vaporeon': 20,
            'Jolteon': 20,
            'Flareon': 20,
            'Porygon': 20,
            'Omanyte': 20,
            'Omastar': 20,
            'Kabuto': 20,
            'Kabutops': 20,
            'Aerodactyl': 20,
            'Snorlax': 25,
            'Articuno': 300,
            'Zapdos': 300,
            'Moltres': 300,
            'Dratini': 10,
            'Dragonair': 20,
            'Dragonite': 30,
            'Mewtwo': 500,
            'Mew' : 500,    
        }
        return points.get(pokemon_name, 0)

        
    def update_leaderboard(self, username: str, points: int) -> None:
        for entry in self.leaderboard:
            if entry['username'] == username:
                entry['points'] = int(entry['points']) + points  # Convert points to integer before updating
                break
        else:
            self.leaderboard.append({'username': username, 'points': points})

        self.leaderboard.sort(key=lambda x: x['points'], reverse=True)
        self.save_leaderboard_data()  # Save leaderboard data to JSON
        self.save_data()  # Save all data

    def save_pokeballs_data(self) -> None:
        with open('pokeballs.json', 'w') as f:
            json.dump(self.user_bags, f)

    def load_pokeballs_data(self) -> None:
        try:
            with open('pokeballs.json', 'r') as f:
                self.user_bags = json.load(f)
        except FileNotFoundError:
            self.user_bags = {}

    def save_caught_pokemon_data(self) -> None:
        with open('caught_pokemon.json', 'w') as f:
            json.dump(self.caught_pokemon, f)

    def load_caught_pokemon_data(self) -> None:
        try:
            with open('caught_pokemon.json', 'r') as f:
                self.caught_pokemon = json.load(f)
        except FileNotFoundError:
            self.caught_pokemon = {}

    def save_leaderboard_data(self) -> None:
        with open('leaderboard.json', 'w') as f:
            json.dump(self.leaderboard, f)

    def load_leaderboard_data(self) -> None:
        try:
            with open('leaderboard.json', 'r') as f:
                self.leaderboard = json.load(f)
        except FileNotFoundError:
            self.leaderboard = []

    def save_data(self) -> None:
        self.save_pokeballs_data()
        self.save_caught_pokemon_data()
        self.save_leaderboard_data()

    def load_data(self) -> None:
        self.load_pokeballs_data()
        self.load_caught_pokemon_data()
        self.load_leaderboard_data()

    async def on_user_leave(self, user: User) -> None:
        while True:
            try:
                print(f"\033[1;35m {user.username} Left the Room\033[0m")
                await self.highrise.chat(f"Thank you for visiting us @{user.username} !")
                break 
            except Exception:
                print("\033[1;31m Leaving failed. Retrying in 5 seconds...\033[0m")
                await asyncio.sleep(5)
                break

if __name__ == '__main__':
    # Add your main script logic here
    print("Main script is running...")
    bot = Bot()
    asyncio.run(bot.handle_network_errors(max_retries=100, retry_delay=5))