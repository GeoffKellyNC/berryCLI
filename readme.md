# **Berry CLI Tools**

Notes:
- Make sure to run the following command to install virtual python env before installing requirements.txt file. Add this to your .gitignore
- `python3 -m venv [envName]`
- You must make a file in the root directory called config.json. In there will house your api keys. MAKE SURE TO ADD THIS TO YOUR .gitignore 
- `{"OPEN_AI_KEY": "KEY_HERE", "POKEMON_RAPID_API_KEY": "KEY HERE", "GOVEE_API_KEY": "KEY_HERE", "LIFEX_API_KEY": "KEY HERE", "YOUTUBE_DATA_KEY": "KEY HERE"}`



## System Commands
These commands start with ++. 

    Home -> ++[command]

### System Commands:
	

 - ++b: This will take you back to the previous module
 - ++kill: This will kill the program entirely. (Can be run from anywhere in the program)
 - ++h: This will take you to the system help menu.
 - ++hm: This will take you to the help menu for your specific module
 - ++clear: This will clear your console. (Will not clear current location)
 
 ## **MODULES**
   1. GPT 
	   - `Home -> gpt`
   2. Poke
	    - `Home -> poke`
   3. Device
	   - `Home -> device`
   4.  Config
	    - `Home -> config`

> ### GPT

 - [x] **Sys commands**. (These still need ++ but build ontop of earlier mentioned ones.)
	 - ++md: This returns as list of available models using the [Open AI API](https://platform.openai.com/docs/introduction)
	 - ++cx: This will return the current context array if there is any.
 - [x] **GPT Commands**. These do not require the ++ prefix  `GPT -> [command]`
	  - [**turbo**] - This will enable you to chat with the chat GPT-3-Turbo Model. Simply ask a question and the ai will return a response
	  - [**recipe**] - This will put you into recipe mode. You will first be asked for a modifier. After you will be asked to enter items. Enter one item per prompt. When done type 'done' and you will be show a list of the items entered. GPT will return a recipe using the ingredients given. Some modifiers can be used together. Up to a limit of 3
		  ### Recipe Modifiers:
			  - g: General Tag: This does not apply any special properties to the request
			  - h: Healthy Tag: This applies a healthy flag to the request to come up with a healthier option.
			  - s: Savings Tag: This applies a savings flag that will try to incorporate ingredients or methods that save money.
			  - q: Quick Tag: This applies the quick flag. This will prompt a recipe that is quicker to prepare.

> ### Device
	

 - [ ] **Sys Commands**

	
			  
			  
		  
