import os.path
import os
import sys
import time

from random import randint
from telegram.ext import Updater
updater = Updater(token='207340155:AAGAr-oxqdv6rlmPot0PlmsV20f7B2EVMWQ')

dispatcher = updater.dispatcher

playerslooking=[]
playersplaying=[]

MAIN = 'GamerBot\\'
GAMES = MAIN+'Profiles\Games\\'
ACCOUNTS = MAIN+'Profiles\Accounts\\'
GENERAL = MAIN+'General\\'
RULES = GENERAL+'Rules\\'
REPORTS = GENERAL+'Reports\\'

#Telegram Based Functions
def start(bot, update):
	
	#createDirectories()
	
	messagestring='.:Message Information:.\n'
	messagestring+='Text: '+update.message.text
	messagestring+='Chat_Id: '+update.message.chat_id
	messagestring+='Username: '+update.message.chat.username

	messagestring+='Update ID: '+ update.update_id
	messagestring+='Message ID: '+update.message.message_id
	messagestring+='From_User ID: '+update.message.from_user.id
	messagestring+='From_User First Name: '+update.message.from_user.first_name
	messagestring+='From_User Last Name: '+update.message.from_user.last_name
	messagestring+='From_User Username: '+update.message.from_user.username
	messagestring+='Chat First Name: '+update.message.chat.first_name
	messagestring+='Chat Last Name: '+update.message.chat.last_name
	messagestring+='Chat Username: '+update.message.chat.username
	messagestring+='Date: '+update.message.date
	messagestring+='Message/Text: '+update.message.text 

	bot.sendMessage(chat_id=update.message.chat_id, text=messagestring)

def echo(bot, update):
	r = randint(0,3)
	if(update.message.new_chat_participant):
		if (r==0):
			bot.sendMessage(chat_id=update.message.chat_id, text='Ooooh! A new person! I love meeting new people! Come and have a chat with me! I love talking about /help and /rules!')
		elif (r==1):
			bot.sendMessage(chat_id=update.message.chat_id, text='FRESH VICTI-... uh... Welcome to the gamer chat! Lets have a quick chat about /help and /rules!')
		else:
			bot.sendMessage(chat_id=update.message.chat_id, text='A new person to play games with! Talk to me with /help and /rules and we\'ll have you playing games with people in no time!')
	elif(update.message.left_chat_participant):
		if (r==0):
			bot.sendMessage(chat_id=update.message.chat_id, text='Looks like there\'s one less gamer to play with...')
		elif (r==1):
			bot.sendMessage(chat_id=update.message.chat_id, text='Oh dear! I hope everything\'s alright...')
		else:
			bot.sendMessage(chat_id=update.message.chat_id, text='Well !@#$...')
	else:
		if (r==0):
			bot.sendMessage(chat_id=update.message.chat_id, text='Hi! I\'m not quite sure what you\'re looking for, maybe you can type /help so I can show you some commands')
		elif (r==1):
			bot.sendMessage(chat_id=update.message.chat_id, text='I think you spelled a command wrong... It\'s okay! I failed at basic English, too...')
		else:
			bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text + ' to you, too!')

	#print('echo')
		

def rules(bot, update, args):
	if not (update.message.chat.username=='' or update.message.chat.username==' '):
		request = ' '.join(args)
		categories='categories'
		if(request.lower()==categories.lower()):
			bot.sendMessage(chat_id=update.message.chat_id, text='Rules: Guidelines\n\nGuidelines are set to encourage proper conduct and use of chat features. For example, Guidelines will cover how to appropriately use the GamerBot and how to properly name your games so that others may find them.')
			bot.sendMessage(chat_id=update.message.chat_id, text='Rules: Lenient\n\nLenient Rules are a general guideline. It is perfectly acceptable to do things listed here, but excessive amounts of it may annoy other members and may see the rule moved to \'Strict\' classification')
			bot.sendMessage(chat_id=update.message.chat_id, text='Rules: Strict\n\nStrict Rules are to be followed at all times. Breaking these rules will result in a suitable form of punishment depending on the rule broken and how severely it was broken.')
		else:
			if(os.path.isfile(RULES+'guiderules.txt')):
				with open(RULES+'guiderules.txt', 'r') as f:
					rules = f.read().splitlines()
				rulestring=''
				for r in rules:
					rulestring+=r+'\n'
				bot.sendMessage(chat_id=update.message.chat_id, text='Bot Usage Guidelines\n'+rulestring)
			else:
				open(RULES+'guiderules.txt', 'a')
			if(os.path.isfile(RULES+'lenientrules.txt')):
				with open(RULES+'lenientrules.txt', 'r') as f:
					rules = f.read().splitlines()
				rulestring=''
				for r in rules:
					rulestring+=r+'\n'
				bot.sendMessage(chat_id=update.message.chat_id, text='Rules: Lenient\n'+rulestring)
			else:
				open(RULES+'lenientrules.txt', 'a')

			if(os.path.isfile(RULES+'strictrules.txt')):
				with open(RULES+'strictrules.txt', 'r') as f:
					rules = f.read().splitlines()
				rulestring=''
				for r in rules:
					rulestring+=r+'\n'
				bot.sendMessage(chat_id=update.message.chat_id, text='Rules: Strict\n'+rulestring)
			else:
				open(RULES+'strictrules.txt', 'a')
				
			bot.sendMessage(chat_id=update.message.chat_id, text='If you want to find out the meaning of each category, type /rules categories')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='For a list of rules, please use /rules in a private chat with me')
		

def suggest(bot, update, args):
	createDirectories()
	command=' '.join(args)
	if command==' ' or command=='':
		bot.sendMessage(chat_id=update.message.chat_id, text='I have suggested nothing to the developers. What a progressive society we live in!')
	else:
		suggestion = ' '.join(args)
		createSuggestion(update.message.from_user.username, suggestion)
		bot.sendMessage(chat_id=update.message.chat_id, text='Thanks for the suggestion! We\'ll see if we can get around to working on it. If we need to clarify anything we\'ll come straight to you!')

def bug(bot, update, args):
	command=' '.join(args)
	if command==' ' or command=='':
		bot.sendMessage(chat_id=update.message.chat_id, text='No bugs to report?! Amazing! I\'m glad that I am a bug-free bot!')
	else:
		report = ' '.join(args)
		createBugReport(update.message.from_user.username, report)
		bot.sendMessage(chat_id=update.message.chat_id, text='Thanks for your bug report! If we have any questions, we\'ll contact you!')

def help(bot, update, args):

	if not (update.message.chat.username=='' or update.message.chat.username==' '):
		command = ' '.join(args)
		if command==' ' or command=='':
			bot.sendMessage(chat_id=update.message.chat_id, text='Hi! I\'m FurryGamerBot! I\'ve been created to help you guys keep track of games you play and connect you as social gamers!')
			bot.sendMessage(chat_id=update.message.chat_id, text='Usable commands are:\n/showallgames\n/showgamers\n/addme\n/removeme\n/showgamesfor\n/addmygame\n/removemygame\n/mygames\n/comparegameswith\n/whoplays\n/addaccount\n/editaccount\n/removeaccount\n/showmyaccounts\n/showaccountsfor\n/addgrouplink\n/editgrouplink\n/removegrouplink\n/showgrouplinks\n/looking\n/notlooking\n/playing\n/notplaying\n/showplayers\n\nIf you would like more help on how to use these commands, you can type /help [command] for more information on that command')
		elif ('suggest' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /suggest sentence\n\nUsing this command you can make a suggestion to improve what I can do for you, or to make features that could be awesome!\n\nFor Example: /suggest your bot can be improved')
		elif ('bug' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /bug sentence\n\nUsing this command you can tell the developers if there is an issue with me so that they can fix me.\n\nFor Example: /bug your bot sucks')
		elif ('showgamesfor' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showgamesfor TagName\n\nYou can use another gamer\'s Telegram @ tag to see what games they own and play... If they have a record, of course.\n\nFor Example: /showgames Bob')
		elif ('showallgames' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showallgames\n\nThis shows all the games that are recorded in our lists.')
		elif ('showgamers' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showgamers\n\nThis shows all the gamers who I currently have a record on.')
		elif ('addme' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /addme\n\nWith this command I can create you your own personal file so you can add games and accounts!')
		elif ('removeme' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /removeme\n\nIf you\'re finished playing with us or want to completely wipe your file, use this command to delete your record.')
		elif ('addmygame' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /addmygame Game, Game, Game, ...\n\nYou can use this function to add games to you personal list. You can add multiple games by separating them with a comma!\n\nFor Example: /addmygame League of Legends, Dark Souls, Defense of the Ancients 2')
		elif ('removemygame' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /removemygame Game, Game, Game, ...\n\nYou can use this function to remove games from you personal list. You can remove multiple games by separating them with a comma!\n\nFor Example: /removemygame League of Legends')
		elif ('mygames' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /mygames\n\nShows a list of all the games in your profile!')
		elif ('comparegameswith' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /comparegameswith TagName\n\nWhen you use this command with another user\'s @ Tag, I will show you what games you and this person have in common!\n\nFor Example: /comparegameswith Alice')
		elif ('whoplays' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /whoplays Game, Game, Game, ...\n\nWhen you use this command and give me a name of some games, I will display all of the players that have that same game!\n\nFor Example: /whoplays League of Legends, Starcraft 2, Diablo 3')
		elif ('notlooking' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /notlooking\n\nNo longer looking for a game? If so, just type this command and I\'ll remove you from the looking list')
		elif ('looking' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /looking Game\n\nLooking for a game? Just type /looking and I\'ll put you in a list of people looking for a game. You can add a game if you\'re looking to play a specific game.\n\nFor Example: /looking League of Legends')
		elif ('notplaying' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /notplaying\n\nFinished playing your game? Enter this command I\'ll remove you from the playing list so people don\'t get the wrong impression!')
		elif ('playing' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /playing Game\n\nPlaying a game and want people to know? (Maybe so they can join you!) If you enter this command I will put you into the playing list.\n\nFor Example: /playing Defense of the Ancients 2')
		elif ('addAccount' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /addaccount ServiceName, AccountName\n\nIf you would like to add a gaming account to your profile, you can use this command by telling me what Service your account is with, and the name of your Account.\n\nFor example: /addAccount Steam, BestBotEva')
		elif ('editAccount' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /editaccount ServiceName, AccountName\n\nWant to edit the name of an account? Just use this command and give me the Service the Account belongs to and the name of the Account.\n\nFor Example: /editAccount Steam, JustAFurryBot')
		elif ('removeAccount' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /editaccount ServiceName\n\nNo longer want to include your account? No biggy! Just enter /removeAccount and the Service that the Account belongs to and I\'ll get rid of it for you!\n\nFor Example: /removeAccount Steam')
		elif ('showmyaccounts' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showmyaccounts\n\nDisplays all of the accounts you have included in your accounts list.')
		elif ('showaccountsfor' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showaccountsfor GamerName\n\nShows accounts for the specified gamer.\n\nFor Example: /showaccountfor thebestgamer')
		elif ('looking' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /looking Game\n\nSet yourself as looking to play a game. You may choose to add a Game after /looking to show others you are looking to play a specific game.\n\nFor Example: /looking Defense of the Ancients 2')
		elif ('notlooking' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /notlooking\n\nRemove yourself from the list of people who are looking to play a game')
		elif ('playing' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /playing Game\n\nSet yourself as playing a game. You may choose to add a Game after /playing to show others you are playing a specific game.\n\nFor Example: /looking Defense of the Ancients 2')
		elif ('notplaying' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /notplaying\n\nRemove yourself from the list of people who are playing games')
		elif ('showplayers' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showplayers\n\nShows everyone who is looking for a game and everyone playing games')
		elif ('addmyaccount' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /addmyaccount ServiceName, AccountName\n\nAdd a gaming service account to your profile. First include the Service Name (e.g., Steam) and then the Account Name.\n\nFor Example, /addmyaccount Steam, MyAccountName\n\nNote that for Account Name, you may want to put in what gamers may use to add you as a friend')
		elif ('editmyaccount' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /editmyaccount ServiceName, AccountName\n\nEdit a gaming service account in your profile. This command will search for the entry of ServiceName and change the AccountName to the new name.\n\nFor Example, /editmyaccount Steam, MyNewAccountName\n\nThis command will change your Steam account from MyAccountName to MyNewAccountName')
		elif ('removemyaccount' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /removemyaccount ServiceName\n\nRemove a gaming service account from your profile. You only need to supply the name of the service.\n\nFor Example, /removemyaccount Steam')
		elif ('addgrouplink' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /addgrouplink GroupName, InviteLink\n\nHave a group for a specific game? Why not add the link here so people can easily find it?\n\nFor Example, /addgrouplink MyGroupName, InviteLink')
		elif ('editgrouplink' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /editgrouplink GroupName, InviteLink\n\nIf you need to change the invite link for your group, you can use this command with the name of your group to change the Invite Link\n\nFor Example, /editgrouplink MyGroupName, NewInviteLink')
		elif ('removegrouplink' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /removegrouplink GroupName\n\nIf you no longer wish to feature your group in the list, you can use /removegrouplink with your GroupName to remove the link permanently.\n\nFor Example, /removegrouplink MyGroupName')
		elif ('showgrouplinks' in command):
			bot.sendMessage(chat_id=update.message.chat_id, text='Usage: /showgrouplinks\n\nThis command will display all invite links to other listed telegram chats.')
		else:
			r = randint(0,4)
			if (r==0):
				bot.sendMessage(chat_id=update.message.chat_id, text='Whatever that is, I can\'t help you with it...')
			elif (r==1):
				bot.sendMessage(chat_id=update.message.chat_id, text='I think we all need a little help...')
			elif (r==2):
				bot.sendMessage(chat_id=update.message.chat_id, text='You are beyond my help...')
			elif (r==3):
				bot.sendMessage(chat_id=update.message.chat_id, text='Help yourself...')
				bot.sendMessage(chat_id=update.message.chat_id, text='to a good education!')
			bot.sendMessage(chat_id=update.message.chat_id, text='To be honest, I did\'t understant what you wanted help with. If you don\'t remember what command you wanted help with, just type /help and I\'ll give you a list of commands I can help you with!')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='For help, please use /help in a private chat with me')

def showallgames(bot, update, args):
	command=' '.join(args)
	if command==' ' or command=='':
		gameslist = ''
		for g in readGamesList():
			gameslist+=g+'\n'
		bot.sendMessage(chat_id=update.message.chat_id, text='Here is a list of games that are owned by all members in my records.\n\n'+gameslist)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='Uhhh... did you mean showgamesfor? I\'ll get you the games for that person instead.')
		showgamesfor(args)
	
def addgame(bot, update, args):
	createDirectories()
	bot.sendMessage(chat_id=update.message.chat_id, text='This function is no longer in use, please use /addmygame instead')
#	command=' '.join(args)
#	if command==' ' or command=='':
#		bot.sendMessage(chat_id=update.message.chat_id, text='I have added nothing to the main games list. You may want to try /addgame game or /addmygame if you\'re looking to add a game to your own personal profile!')
#	else:
#		game = ' '.join(args)
#		appendGamesList(game)
#		bot.sendMessage(chat_id=update.message.chat_id, text=game+' has been added to the games list!')

def removegame(bot, update, args):
	bot.sendMessage(chat_id=update.message.chat_id, text='This function is no longer in use, please use /removemygame instead')
#	command=' '.join(args)
#	if command==' ' or command=='':
#		bot.sendMessage(chat_id=update.message.chat_id, text='I have removed nothing to the main games list. You may want to try /removegame game or /removemygame if you\'re looking to add a game to your own personal profile!')
#	else:
#		game = ' '.join(args)
#		removeFromGamesList(game)
#		bot.sendMessage(chat_id=update.message.chat_id, text=game+' has been removed from the games list!')
	
def showgamers(bot, update):
	gamerlist = ''
	for g in readGamersList():
		gamerlist+=g+'\n'
	if not gamerlist:
		bot.sendMessage(chat_id=update.message.chat_id, text='There are no gamers in this list')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='Here is a list of gamers\n\n'+gamerlist)

def addme(bot, update):
	createDirectories()
	result = createGamerProfile(update.message.from_user.username)
	
	if (result==0):
		bot.sendMessage(chat_id=update.message.chat_id, text='You already seem to exist in the Gamer List! Try adding some games to your list using /addmygame')
	elif (result==1):
		bot.sendMessage(chat_id=update.message.chat_id, text='Done! I\'ve added you to the list, you can start adding games using the /addmygame command!')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='You\'re not in the list and I still couldn\'t create your file! Something\'s gone horribly, horribly wrong!')
	
def removeme(bot, update):
	result = removeGamerProfile(update.message.from_user.username)
	if (result==0):
		bot.sendMessage(chat_id=update.message.chat_id, text='I could not delete you from the Gamer list even though your file is visible, please talk to someone who can solve this issue!')
	elif (result==1):
		bot.sendMessage(chat_id=update.message.chat_id, text='I have now removed you from the Gamer list, thanks for playing!')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='You don\'t seem to have a file that I can remove...')
	
def showgamesfor(bot, update, args):
	command=' '.join(args)
	if command==' ' or command=='':
		bot.sendMessage(chat_id=update.message.chat_id, text='Now showing nobodies games. If you\'d like to show games for a specific gamer, you can type /showgamesfor gamer')
	else:
		target = ' '.join(args)
		games = getGamesForProfile(target)
		if not games:
			bot.sendMessage(chat_id=update.message.chat_id, text='That gamer doesn\'t have any games! What a shame...')
		else:
			bot.sendMessage(chat_id=update.message.chat_id, text='Here is a list of games that '+target+' plays:\n')
			gamestring = ''
			for g in games:
				gamestring+=g + '\n'
			bot.sendMessage(chat_id=update.message.chat_id, text=gamestring)	

def mygames(bot, update):
	command=' '.join(args)
	exists = checkUserExists(update.message.from_user.username)
	if(exists==1):
		if command==' ' or command=='':
			bot.sendMessage(chat_id=update.message.chat_id, text='Now showing nobodies games. If you\'d like to show games for a specific gamer, you can type /showgamesfor gamer')
		else:
			games = getGamesForProfile(update.message.from_user.username)
			if not games:
				bot.sendMessage(chat_id=update.message.chat_id, text='You don\'t seem to have any games added, you can add games with the /addmygame command!')
			else:
				bot.sendMessage(chat_id=update.message.chat_id, text='Here is a list of your games.\n')
				gamestring = ''
				for g in games:
					gamestring+=g + '\n'
				bot.sendMessage(chat_id=update.message.chat_id, text=gamestring)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='You don\'t seem to have an account. You can make one with the /addme command!')
		

def addmygame(bot, update, args):
	createDirectories()
	games=' '.join(args)
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		if games==' ' or games=='':
			bot.sendMessage(chat_id=update.message.chat_id, text='I have added nothing to your profile. I can add a game to your profile with the command /addmygame game')
		else:
			games = games.split(', ')
			addedgames = addGamesToProfile(update.message.from_user.username, games)
			gamestring = ''
			for g in games:
				for a in addedgames:
					if (a.lower()==g.lower()):
						gamestring += g + ', '
			bot.sendMessage(chat_id=update.message.chat_id, text='I have added ' + gamestring + 'to your profile!')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='Before you can add a game, you will need to create a profile! It\'s simple! Just type /addme')

def removemygame(bot, update, args):
	command=' '.join(args)
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		if command==' ' or command=='':
			bot.sendMessage(chat_id=update.message.chat_id, text='I have removed nothing from your profile. I can remove a game from your profile with the command /removemygame game')
		else:
			games = ' '.join(args)
			result = removeGamesFromProfile(update.message.from_user.username, games)
			games = games.split(', ')	
			if not result:
				bot.sendMessage(chat_id=update.message.chat_id, text='I didn\'t manage to delete any of those games, are you sure those games are in your list and you didn\'t make any spelling errors?')
			else:
				gamestring = ''
				for g in games:
					for r in result:
						if (r.lower()==g.lower()):
							gamestring += g + ', '
				bot.sendMessage(chat_id=update.message.chat_id, text='I have removed ' + gamestring + 'from your list!')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='Before you can remove a game, you will need to create a profile! It\'s simple! Just type /addme')

def comparegameswith(bot, update, args):
	command=' '.join(args)
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		if command==' ' or command=='':
			but.sendMessage(chat_id=update.message.chat_id, text='You have no games in common with a nameless person. If you want to compare games to someone, you can type /comparegameswith gamer')
		else:
			othergamer = ' '.join(args)
			result = compareGamesToProfile(update.message.from_user.username, othergamer)
			gamestring=''
			print('out')
			for r in result:
				gamestring+=r+', '
			bot.sendMessage(chat_id=update.message.chat_id, text='You share these games with '+othergamer+'\n'+gamestring)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='Before you can compare games with another gamer, you will need to create a profile! It\'s simple! Just type /addme')

def whoplays(bot, update, args):
	command=' '.join(args)
	if command==' ' or command=='':
		bot.sendMessage(chat_id=update.message.chat_id, text='I think there\'d be very few gamers here who don\'t play anything. Did you want me to see who plays a game? Try /whoplays game')
	else:
		games = ' '.join(args).split(', ')
		result = getGamersWhoPlay(games)
		print('out')
		for res in result:
			messagestring=('Gamers who play ' )
			first = 0
			for r in res:
				messagestring += r
				if(first==0):
					messagestring += "\n"
				else:
					messagestring += ', ' 
				first = 1
			
			bot.sendMessage(chat_id=update.message.chat_id, text=messagestring)

def looking(bot, update, args):
	game = ' '.join(args)
	if game=='' or game==' ':
		playerslooking.append(update.message.from_user.username)
		bot.sendMessage(chat_id=update.message.chat_id, text='I have set you as looking to play anything')
	else:
		playerslooking.append(update.message.from_user.username + ' is looking for a game of ' + game)
		bot.sendMessage(chat_id=update.message.chat_id, text='I have set you as looking to play ' + game)
		

def notlooking(bot, update):
	deleted=0
	index=0
	for player in playerslooking:
		if(update.message.from_user.username==player):
			del playerslooking[index]
			bot.sendMessage(chat_id=update.message.chat_id, text='I have removed you from the looking list')
			deleted=1
		index=index+1
	if deleted==0:
		bot.sendMessage(chat_id=update.message.chat_id, text='You don\t seem to be playing anything...')
			
def showplayers(bot, update):
	messagestring='Players who are looking for a game:\n\n'
	for player in playerslooking:
		messagestring = messagestring + player
	bot.sendMessage(chat_id=update.message.chat_id, text=messagestring)

	messagestring='Players who are playing a game:\n\n'
	for player in playersplaying:
		messagestring = messagestring + player
	bot.sendMessage(chat_id=update.message.chat_id, text=messagestring)

def playing(bot, update, args):
	game = ' '.join(args)
	if game=='' or game==' ':
		playersplaying.append(update.message.from_user.username + ' is playing games')
		bot.sendMessage(chat_id=update.message.chat_id, text='I have set you as playing games')
	else:
		playersplaying.append(update.message.from_user.username + ' is playing ' + game)
		bot.sendMessage(chat_id=update.message.chat_id, text='I have set you as playing ' + game)

def notplaying(bot, update):
	deleted=0
	index=0
	for player in playersplaying:
		if(update.message.from_user.username.lower()==player.lower()):
			del playersplaying[index]
			bot.sendMessage(chat_id=update.message.chat_id, text='I have removed you from the playing list')
			deleted=1
		index=index+1
	if deleted==0:
		bot.sendMessage(chat_id=update.message.chat_id, text='You don\'t seem to be playing anything...')

def addmyaccount(bot, update, args):
	createDirectories()
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		delimited = ' '.join(args).split(', ')
		result = addGamerAccount(update.message.from_user.username, delimited[0], delimited[1])
		if (result==1):
			bot.sendMessage(chat_id=update.message.chat_id, text='I have added the following account to your profile:\n\n' + delimited[0] + ' - ' + delimited[1])
		else:
			bot.sendMessage(chat_id=update.message.chat_id, text='I could not add that account to your profile, something has gone wrong')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='To add an account, you\'ll need to make a profile. I can make one for you with the /addme command!')

def editmyaccount(bot, update, args):
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		delimited = ' '.join(args).split(', ')	
		result = editGamerAccount(update.message.from_user.username, delimited[0], delimited[1])
		bot.sendMessage(chat_id=update.message.chat_id, text='I have edited the following account in your profile:\n\n' + delimited[0] + ' - ' + delimited[1])
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='To edit an account, you\'ll need to make a profile. I can make one for you with the /addme command!')

def removemyaccount(bot, update, args):
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		account = ' '.join(args).split(', ')
		result = removeGamerAccount(update.message.from_user.username, account[0])
		bot.sendMessage(chat_id=update.message.chat_id, text='I have removed the following account from your profile:\n\n' + account[0])
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='To remove an account, you\'ll need to make a profile. I can make one for you with the /addme command!')

def showmyaccounts(bot, update, args):
	exists = checkUserExists(update.message.from_user.username)
	if (exists==1):
		accounts = getAccountsForProfile(update.message.from_user.username)
		accountstring = ''
		if not accounts:
			bot.sendMessage(chat_id=update.message.chat_id, text='You don\'t seem to have any accounts in your profile. You can add accounts to your profile by using /addmyaccount [Service] [Account]')
		else:
			for account in accounts:
				accountstring+=account+'\n'
			bot.sendMessage(chat_id=update.message.chat_id, text='Accounts listed in your profile:\n' + accountstring)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='To view your accounts, you\'ll need to make a profile and add accounts to your account list. I can make a profile for you with the /addme command and add accounts to your profile with /addmyaccount!')		

def showaccountsfor(bot, update, args):
	target = ' '.join(args)
	exists = checkUserExists(target)
	if (exists==1):
		accounts = getAccountsForProfile(target)
		accountstring = ''
		if not accounts:
			bot.sendMessage(chat_id=update.message.chat_id, text=target + ' does not seem to have any accounts written in their profile.')
		else:
			for account in accounts:
				accountstring+=account+'\n'
			bot.sendMessage(chat_id=update.message.chat_id, text='Accounts listed in ' + target +'\'s profile:\n' + accountstring)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='That person does not seem to have a record in my list.')		
		
def addgrouplink(bot, update, args):
	createDirectories()
	link = ' '.join(args).split(', ')
	addGroupLink(link[0], link[1])
	bot.sendMessage(chat_id=update.message.chat_id, text='I have added the following group link to the list of groups\n\n' + link[0] + ' - ' + link[1])

def editgrouplink(bot, update, args):
	link = ' '.join(args).split(', ')
	editGroupLink(link[0], link[1])
	if(result==1):
		bot.sendMessage(chat_id=update.message.chat_id, text='I have edited the following group link in the list of groups\n\n' + link[0] + ' - ' + link[1])
	elif(result==2):
		bot.sendMessage(chat_id=update.message.chat_id, text='I was not able to edit the link for you, are you sure the link is spelled correctly and exists in the list?')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='There doesn\'t seem to be any links to be edited')
	
def removegrouplink(bot, update, args):
	remove = ' '.join(args)
	result = removeGroupLink(remove)
	if(result==1):
		bot.sendMessage(chat_id=update.message.chat_id, text='I have removed the following group link removed the list of groups\n\n' + remove)
	elif(result==2):
		bot.sendMessage(chat_id=update.message.chat_id, text='I was not able to remove the link for you, are you sure the link is spelled correctly and exists in the list?')
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='There doesn\'t seem to be any links to be deleted')
	
def showgrouplinks(bot, update):
	links = showGroupLinks()
	if not (links==0):
		linkstring=''
		for link in links:
			linkstring=link+'\n'
		bot.sendMessage(chat_id=update.message.chat_id, text='Here is a list of links to other groups:\n'+linkstring)
	else:
		bot.sendMessage(chat_id=update.message.chat_id, text='There are no links to list.')
	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions
#Internal Functions	
#Internal Functions	

#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	

#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions	
#Internal Functions

def createSuggestion(suggester, suggestion):
	suggestionstring = time.strftime("%d%m%Y") + ': ' + suggester + ' - ' + suggestion
	if (os.path.isfile(REPORTS+'suggestions.txt')):
		with open(REPORTS+'suggestions.txt', 'r') as f:
			suggestions = f.read().splitlines()
		suggestions.append(suggestionstring)
		with open(REPORTS+'suggestions.txt', 'w') as f:
			for s in suggestions:
				f.write(s +'\n')
	else:
		open(REPORTS+'suggestions.txt', 'a')
		with open(REPORTS+'suggestions.txt', 'w') as f:
			f.write(suggestionstring)
			
def createBugReport(reporter, report):
	reportstringstring = time.strftime("%d%m%Y") + ': ' + reporter + ' - ' + report
	if (os.path.isfile(REPORTS+'bugs.txt')):
		with open(REPORTS+'bugs.txt', 'r') as f:
			reports = f.read().splitlines()
		reports.append(reportstring)
		with open(REPORTS+'bugs.txt', 'w') as f:
			for s in reports:
				f.write(s +'\n')
	else:
		open(REPORTS+'reports.txt', 'a')
		with open(REPORTS+'reports.txt', 'w') as f:
			f.write(reportstring)

def readGamesList():
	if not(os.path.isfile(GENERAL+'gameslist.txt')):
		open(GENERAL+'gameslist.txt', 'a')
	with open(GENERAL+'gameslist.txt', 'r') as f:
		games = f.read().splitlines()
		return games
	
def appendGamesList(game):
	games = readGamesList()
	result = stopDuplicate(game, games)
	if(result==0):
		games.append(game)
		removeDuplicates(games)
		games.sort()
		with open(GENERAL+'gameslist.txt', 'w') as f:
			for g in games:
				f.write(g+'\n')
	
		
def removeFromGamesList(game):
	deleted = 0;
	index= 0;
	games = readGamesList()
	for g in games:
		if (g.lower()==game.lower()):
			deleted = 1
			del games[index]
		index=index+1
	if (deleted==1):
		with open(GENERAL+'gameslist.txt', 'w') as f:
			for g in games:
				f.write(g+'\n')	
	elif (deleted==0):
		print ("Game not found")
		
def readGamersList():
	if(os.path.isfile(GENERAL+'gamerslist.txt')):
		with open(GENERAL+'gamerslist.txt', 'r') as f:
			gamers = f.read().splitlines()
			return gamers
	else:
		open(GENERAL+'gamerslist.txt', 'a')
		with open(GENERAL+'gamerslist.txt', 'r') as f:
			gamers = f.read().splitlines()
			return gamers
	
	
		
def appendGamersList(gamer):
	gamers = readGamersList()
	gamers.append(gamer)
	gamers.sort()
	with open(GENERAL+'gamerslist.txt', 'w') as f:
		for g in gamers:
			f.write(g+'\n')
			
def removeFromGamersList(gamer): 
	print('Removing ' + gamer)
	deleted = 0;
	index= 0;
	gamers = readGamersList()
	for g in gamers:
		print (g)
		if (g.lower()==gamer.lower()):
			print ('destroy' + g)
			deleted = 1
			del gamers[index]
		index=index+1

	if (deleted==1):
		with open(GENERAL+'gamerslist.txt', 'w') as f:
			for g in gamers:
				f.write(g+'\n')	
	elif (deleted==0):
		print ("Gamer not found")	

def createGamerProfile(gamer):
	accountfile = ACCOUNTS+gamer+'Accounts.txt'
	if (os.path.isfile(GAMES + gamer + '.txt')):
		return 0
	else:
		print('Making new profile for ' + gamer)
		open((GAMES + gamer + '.txt'), 'a')
		open((accountfile), 'a')
		if (os.path.isfile(GAMES+gamer + '.txt')):
			appendGamersList(gamer)
			return 1
		else:
			return 2

def removeGamerProfile(gamer):
	accountfile = ACCOUNTS+gamer+'Accounts.txt'
	if (os.path.isfile(GAMES+gamer + '.txt')):
		os.remove(GAMES+gamer+'.txt')
		os.remove(accountfile)
		if(os.path.isfile(GAMES+gamer+'.txt')):
			return 0
		else:
			removeFromGamersList(gamer)
			return 1
	else:
		return 2
		
def getGamesForProfile(target):
	gamers = readGamersList()
	print('looking for ' + target)
	for g in gamers:
		print(g)
		if(target.lower()==g.lower()):
			with open((GAMES+target+'.txt'), 'r') as f:
				games = f.read().splitlines()
				return games
	return 0

def addGamesToProfile(gamer, games):
	print('test')
	games = removeDuplicates(games)
	print('test')
	with open((GAMES+gamer+'.txt'), 'r') as f:
		currentgames = f.read().splitlines()
	index=0
	
	print('test')
	for g in games:
		for cg in currentgames:
			if (g.lower()==cg.lower()):
				print (g + ' found as duplicate')
				del games[index]
		index=index+1
	for g in games:
		currentgames.append(g)
	currentgames.sort()
	
	print('test')
	print(GAMES+gamer+'.txt')
	with open((GAMES+gamer+'.txt'), 'w') as f:
		for g in currentgames:
			f.write(g+'\n')
			print('writing')
			appendGamesList(g)
			print('appended')
			
	print('test')
	return currentgames

def removeGamesFromProfile(gamer, games):
	deletedlist = []
	games = games.split(', ')
	games = removeDuplicates(games)
	for g in games:
		print (g)
	with open((GAMES+gamer+'.txt'), 'r') as f:
		currentgames= f.read().splitlines()
	for g in games:
		index=0
		for c in currentgames:
			print (g + ' vs ' + c)
			if (g.lower()==c.lower()):
				deletedlist.append(c)
				print ('deleting ' + currentgames[index])
				del currentgames[index]
			index=index+1
	if deletedlist:
		with open((GAMES+gamer+'.txt'), 'w') as f:
			for g in currentgames:
				f.write(g+'\n')
	return deletedlist
	#Issue, how to update the games list?
	#Best to overwrite entire list with games from files again, costly, may need to schedule process daily/weekly

def compareGamesToProfile(gamer, target):
	gamergames = []
	targetgames = []
	matchedgames = []
	with open((GAMES+gamer+'.txt'), 'r') as f:
		gamergames = f.read().splitlines()
	with open((GAMES+target+'.txt'), 'r') as f:
		targetgames = f.read().splitlines()

	for g in gamergames:
		for t in targetgames:
			if (g.lower()==t.lower()):
				matchedgames.append(t)

	return matchedgames

def getGamersWhoPlay(inputgames):

	inputgames = removeDuplicates(inputgames)
	index=0
	gamerindex = 0
	gamerslist = readGamersList();
	savedgameslist = []
	savedgamername = []
	
	resultlist = []

	for gamer in gamerslist:
		if(gamer=='' or gamer==' '):
			print('false gamer')
		else:
			templist = []
			with open((GAMES+gamer+'.txt'), 'r') as f:
				gameslist = f.read().splitlines()
			print('read games for ' + gamer)
			for game in gameslist:
				for input in inputgames:
					if(input.lower()==game.lower()):
						templist.append(game)
			savedgamername.append(gamer)
			savedgameslist.append(templist)
			for t in templist:
				print(t)
	gameindex=0
	gamerindex=0
	for input in inputgames:
		gamerindex=0
		namelist = []
		namelist.append(input)
		for gameslist in savedgameslist:
			for game in gameslist:
				if(input.lower()==game.lower()):
					namelist.append(savedgamername[gamerindex])
			gamerindex=gamerindex+1
		resultlist.append(namelist)
		
	return resultlist

def addGamerAccount(gamer, account, accountname):
	file = ACCOUNTS + gamer + 'Accounts.txt'
	if (os.path.isfile(file)):
		accounts = getAccountsForProfile(gamer)
		accounts.append(account + ": " + accountname)
		accounts.sort()
		setAccountsForProfile(gamer, accounts)
		return 1
	else:
		open((file), 'a')
		if (os.path.isfile(file)):
			accounts = getAccountsForProfile(gamer)
			for acc in accounts:
				if account.lower()==acc.lower():
					return 3
			accounts.append(account + ": " + accountname)
			accounts.sort()
			setAccountsForProfile(gamer, accounts)
			return 1
		else:
			return 2

def editGamerAccount(gamer, account, accountname):
	file = ACCOUNTS + gamer + 'Accounts.txt'
	if(os.path.isfile(file)): 	
		accounts = getAccountsForProfile(gamer)
		index = 0
		for a in accounts:
			if (account.lower() in a.lower()):
				accounts[index]=account + ': ' + accountname
				setAccountsForProfile(gamer, accounts)
				return 1
			index = index + 1
	else:
		return 0
	return 2
			
def removeGamerAccount(gamer, account):
	file = ACCOUNTS + gamer + 'Accounts.txt'
	if(os.path.isfile(file)):
		accounts = getAccountsForProfile(gamer)
		index = 0
		for a in accounts:
			if (account.lower() in a.lower()):
				del accounts[index]
				accounts.sort()
				setAccountsForProfile(gamer, accounts)
				return 1
			else:
				print('No match')
			index = index+1
	else:
		return 0
	return 2

def addGroupLink(name, link):
	if(os.path.isfile(GENERAL+'grouplinks.txt')):
		with open(GENERAL+'grouplinks.txt', 'r') as f:
			links = f.read().splitlines()
		links.append(name + ' - ' + link)
		links.sort()
		with open(GENERAL+'grouplinks.txt', 'w') as f:
			for l in links:
				f.write(l)
		return 1
	else:
		open(GENERAL+'grouplinks.txt', 'a')
		if(os.path.isfile(GENERAL+'grouplinks.txt')):
			with open(GENERAL+'grouplinks.txt', 'w') as f:
				f.write(name + ' - ' + link)
			return 1
		else:
			return 0

def editGroupLink(name, link):
	if(os.path.isfile(GENERAL+'grouplinks.txt')):
		with open(GENERAL+'grouplinks.txt', 'r') as f:
			links = f.read().splitlines()
		index = 0
		for l in links:
			if (name.lower() in l.lower()):
				links[index] = name + ': ' + link
				with open(GENERAL+'grouplinks.txt', 'w') as f:
					for link in links:
						f.write(link+'\n')
				return 1
			index=index+1
	else:
		return 0
	return 2

def removeGroupLink(name):
	if(os.path.isfile(GENERAL+'grouplinks.txt')):
		with open(GENERAL+'grouplinks.txt', 'r') as f:
			links = f.read().splitlines()
		index = 0
		for l in links:
			if (name.lower() in l.lower()):
				del links[index]
				links.sort()
				with open(GENERAL+'grouplinks.txt', 'w') as f:
					for link in links:
						f.write(link+'\n')
				return 1
			index=index+1
	else:
		return 0
	return 2

def showGroupLinks():
	if(os.path.isfile(GENERAL+'grouplinks.txt')):
		with open(GENERAL+'grouplinks.txt', 'r') as f:
			links = f.read().splitlines()
		return links
	else:
		return 0

#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions

#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions
#Supporting Functions

def checkFor(name, array):
	for a in array:
		if name in a:
			return 1
	return 0
	
def stopDuplicate(game, list):
	for l in list:
		if l.lower()==game.lower():
			return 1
	return 0

def removeDuplicates(games):
	newgames = []
	for g in games:
		duplicated=0
		for n in newgames:
			if (g.lower()==n.lower()):
				duplicated=1
		if (duplicated==0):
			newgames.append(g)
	return newgames

def checkUserExists(username):
	gamers = readGamersList()
	for g in gamers:
		if(g.lower()==username.lower()):
			return 1
	return 0		
	
def getAccountsForProfile(gamer):
	file=ACCOUNTS+gamer+'Accounts.txt'
	if(os.path.isfile(file)):
		with open(file, 'r') as f:
			accounts = f.read().splitlines()
			return accounts
	else:
		open(file, 'a')
		with open(file, 'r') as f:
			accounts = f.read().splitlines()
			return accounts
	
def setAccountsForProfile(gamer, accounts):
	with open(ACCOUNTS+gamer+'Accounts.txt', 'w') as f:
		for a in accounts:
			f.write(a+'\n')
		
	
def createDirectories():
	if not os.path.exists('GamerBot'):
		os.makedirs('GamerBot')
	if not os.path.exists('GamerBot\\Profiles\\Games'):
		os.makedirs('GAmerBot\\Profiles\\Games')
	if not os.path.exists('GamerBot\\Profiles\\Accounts'):
		os.makedirs('GamerBot\\Profiles\\Accounts')
	if not os.path.exists('GamerBot\\General'):
		os.makedirs('GamerBot\\General')
	if not os.path.exists('GamerBot\\General\\Rules'):
		os.makedirs('GamerBot\\General\\Rules')
	if not os.path.exists('GamerBot\\General\\Reports'):
		os.makedirs('GamerBot\\General\\Reports')

#Dispatchers
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('rules', rules)
dispatcher.addTelegramCommandHandler('suggest', suggest)
dispatcher.addTelegramCommandHandler('bug', bug)
dispatcher.addTelegramCommandHandler('help', help)
dispatcher.addTelegramMessageHandler(echo)
dispatcher.addTelegramCommandHandler('showallgames', showallgames)
dispatcher.addTelegramCommandHandler('showgamers', showgamers)
dispatcher.addTelegramCommandHandler('addme', addme)
dispatcher.addTelegramCommandHandler('removeme', removeme)
dispatcher.addTelegramCommandHandler('showgamesfor', showgamesfor)
dispatcher.addTelegramCommandHandler('addmygame', addmygame)
dispatcher.addTelegramCommandHandler('removemygame', removemygame)
dispatcher.addTelegramCommandHandler('comparegameswith', comparegameswith)
dispatcher.addTelegramCommandHandler('whoplays', whoplays)
dispatcher.addTelegramCommandHandler('looking', looking)
dispatcher.addTelegramCommandHandler('notlooking', notlooking)
dispatcher.addTelegramCommandHandler('playing', playing)
dispatcher.addTelegramCommandHandler('notplaying', notplaying)
dispatcher.addTelegramCommandHandler('showplayers', showplayers)
dispatcher.addTelegramCommandHandler('addmyaccount', addmyaccount)
dispatcher.addTelegramCommandHandler('editmyaccount', editmyaccount)
dispatcher.addTelegramCommandHandler('removemyaccount', removemyaccount)
dispatcher.addTelegramCommandHandler('showmyaccounts', showmyaccounts)
dispatcher.addTelegramCommandHandler('showaccountsfor', showaccountsfor)
dispatcher.addTelegramCommandHandler('addgrouplink', addgrouplink)
dispatcher.addTelegramCommandHandler('editgrouplink', editgrouplink)
dispatcher.addTelegramCommandHandler('removegrouplink', removegrouplink)
dispatcher.addTelegramCommandHandler('showgrouplinks', showgrouplinks)

updater.start_polling()

#cd Dev*\Py*
#python MyScripts\FurryGamerBot2.pyy