# Pokémon Highrise Bot

## Overview
The **Pokémon Highrise Bot** is an interactive bot designed for the **Highrise Metaverse**, where users can engage in exciting Pokémon-themed gameplay. Players can catch, collect, and compete for points on a leaderboard, mimicking the core elements of a Pokémon Trainer experience.

---

## Features
- **Interactive Chat Commands**  
  Players can use commands like `Catch`, `Bag`, `Score`, `Board`, and more to interact with the bot and play the game.
  
- **Dynamic Pokémon Encounters**  
  Users encounter wild Pokémon as they explore the environment, with varying catch rates for regular, rare, and legendary Pokémon.

- **Leaderboard System**  
  Tracks player scores based on the Pokémon they’ve caught, fostering a competitive environment.

- **Pokéball Management**  
  Players must manage their inventory of Pokéballs, which can be replenished by tipping the bot in-game.

- **Dynamic Movement**  
  The bot navigates through predefined positions in the Highrise room, creating a lively and engaging atmosphere.

- **Customizable Gameplay**  
  The bot supports additional features like Pokémon tournaments, whisper-based notifications, and emote-based interactions.

---

## Installation
### Prerequisites
- **Python 3.8+**
- **Highrise SDK**
- **Flask**
- **Requests**

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pokemon-highrise-bot
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up a Flask server for keep-alive functionality. This can be hosted locally or on a service like **Replit**.
4. Add your Highrise bot token to the project:
   - Locate the configuration file and insert your bot token for authentication.
5. Run the bot:
   ```bash
   python bot.py
   ```

---

## How to Play
1. Join the Highrise room where the bot is active.
2. Use the following commands to interact with the bot:
   - `Catch` - Attempt to catch a wild Pokémon.
   - `Bag` - Check your current inventory of Pokéballs.
   - `Score` - View your current score.
   - `Board` - See the leaderboard with top players.
   - `Pokelist` - View the last 20 Pokémon you caught.
   - `Pokedex` - Check your complete collection.

3. Encounter wild Pokémon by exploring different areas of the room.  
4. Tip the bot to buy more Pokéballs if needed. 

---

## Gameplay Mechanics
### Pokémon Types and Catch Rates
- **Regular Pokémon**: 50%-80% catch rate.
- **Rare Pokémon**: 30% catch rate.
- **Legendary Pokémon**: 1% catch rate.

### Points System
Each Pokémon has a point value based on its rarity. Points are automatically added to your score upon a successful capture.

### Pokéballs
- Players start with a limited number of Pokéballs.
- Additional Pokéballs can be purchased using in-game tipping.

---

## Developer Guide
### Core Files
- `bot.py`: Main bot logic and event handling.
- `keep_alive.py`: Flask server for uptime monitoring.
- `requirements.txt`: List of dependencies.

### Adding New Features
1. Add new Pokémon or adjust catch rates in the `on_chat` method.  
2. Define additional commands by extending the `on_chat` logic.  
3. Modify room navigation by updating the `self.positions` list.

### Error Handling
The bot includes retry logic for network-related issues and gracefully handles exceptions during gameplay.

---

## Future Improvements
- **Tournament Mode**: Organize Pokémon battles between users.  
- **Item Drops**: Introduce in-game items like berries or special Pokéballs.  
- **Enhanced Leaderboard**: Include detailed stats like rarest Pokémon caught.  
- **Event Triggers**: Add seasonal or location-based Pokémon encounters.

---

## License
This project is open-source and available under the MIT License. Feel free to contribute and make it even better!

---

## Contact
For support or feature requests, feel free to reach out:  
- **Developer**: [Mizhab Ansar](https://www.linkedin.com/in/mizhabansar/)  
- **GitHub**: [haveyoumetmiz](https://github.com/haveyoumetmiz)

--- 
