# ====  File Header Information ====
# Author: Samyak Jain
# Email: samyak0101@gmail.com
# GitHub: https://github.com/samyak0101
# Socials: https://linktr.ee/samyyj

# IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

# VARIABLE DECLARATIONS
CHROME_DRIVER_LOCATION = "C:/Users/<destination to chrome driver>"
USERNAME = "discord username or email"
PASS = "password"
CHANNEL_LINK = "link to the channel where bot will run"

# METHODS

# Creates browser instance, logs into discord and navigates to specified channel link
def openDiscordAndLogin(userEmail, userPass, channelLink, chromeDriverLocation):
    '''
    :param userEmail: The email you wish to use to login to discord
    :param userPass: The password associated with this email for discord login
    :param channelLink: Web link to the channel you wish to open
    :param chromeDriverLocation: File path to the chrome driver
    :return: browser variable containing a referecnce to the browser object used to target the channel
    '''

    driver_path = chromeDriverLocation
    browser = webdriver.Chrome(driver_path)
    browser.get(channelLink)
    # waiting 5 seconds for the discord channel to load (in case internet is slow).
    time.sleep(5)

    # Try catch block to find element first by text id, next by e-mail in case it fails.
    try:
        enterUsername = browser.find_element("[type=text]")
        enterUsername.send_keys(userEmail)
        enterUsername.send_keys(Keys.TAB)

    except:
        enterUsername = browser.find_element("[type=email]")
        enterUsername.send_keys(userEmail)
        enterUsername.send_keys(Keys.TAB)

    enterPassword = browser.find_element("[type=password]")
    enterPassword.send_keys(userPass)
    # Press the login button.
    enterPassword.send_keys(Keys.ENTER)

    # Sleep for browser to load, let it load, and sleep again for time buffer.
    time.sleep(5)
    browser.get(channelLink)
    time.sleep(5)
    # Returns broswer instance
    return browser


# Retrieves the sender of the most recent message in the channel
def getLastMessage(browser, num):
    """
    :param browser: Broswer chrome instance
    :param num: Number of messages to get
    :return: Return string name of author of most recent discord message in channel
    """
    # Gets all text messages  in the channel
    messageMegaBox = browser.find_element_by_xpath("//div[@class='scrollerInner-2YIMLh']").text
    # Divides messages into a list of grammatically correct sentences.
    messageSentences = nltk.sent_tokenize(messageMegaBox)

    # Gets the last 5 messages in the channel
    lastSentences = messageSentences[-5] + messageSentences[-4] + messageSentences[-3] + messageSentences[-2] + \
                    messageSentences[-1]
    # Indexing the last 5 sentences by words to search for specific words
    subFinalMessage = nltk.word_tokenize(lastSentences)

    # Creating a sentence with the most recent occurrence of the word "Today" to get the latest message
    finalMessage = subFinalMessage[0:subFinalMessage.index("Today")]

    # Bot specific code:
    if num == 1:
        finalMessage = subFinalMessage[0:subFinalMessage.index("BOT")]
        finalMessage = finalMessage[::-1]
        finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[4:])
        if (finalMessage == "pause"):
            send("pausing for 60 second", browser)
            time.sleep(60)
        return finalMessage

    if (subFinalMessage.index("BOT") < subFinalMessage.index("SamyToday")):
        #         print("bot index found first bro")
        finalMessage = subFinalMessage[0:subFinalMessage.index("BOT")]
        finalMessage = finalMessage[::-1]
        finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[4:])
        print("Dank Memer: ", finalMessage)
        return "bot"

    elif (subFinalMessage.index("BOT") > subFinalMessage.index("SamyToday")):
        #         print("samy index found first bro")
        finalMessage = subFinalMessage[0:subFinalMessage.index("SamyToday")]
        finalMessage = finalMessage[::-1]
        finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[3:])
        print("Samy: ", finalMessage)

        return "samy"


# Returns the last message in the discord channel
def getNumMessages(browser, messageContainerXPATH, numMessages):
    """

    :param browser: browser chrome instance
    :param messageContainerXPATH: XPATH to the html container that contains all the messages
    :param numMessages: the number of messages to be sent
    :return:
    """
    # Navigates to the messageBox and stores the messages requested by user
    messageMegaBox = browser.find_element_by_xpath(messageContainerXPATH).text
    messageSentences = nltk.sent_tokenize(messageMegaBox)
    # print(messageSentences)
    lastSentences = messageSentences[-12] + messageSentences[-11] + messageSentences[-10] + messageSentences[-9] + \
                    messageSentences[-8] + messageSentences[-7] + messageSentences[-6] + messageSentences[-5] + \
                    messageSentences[-4] + messageSentences[-3] + messageSentences[-2] + messageSentences[-1]
    print("last 5 sentences from getmessages\n", lastSentences)
    subFinalMessage = nltk.word_tokenize(lastSentences)
    subFinalMessage = subFinalMessage[::-1]
    finalMessage = subFinalMessage[0:subFinalMessage.index("Today")]
    finalMessage = finalMessage[::-1]
    finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[3:])
    # returns stored messages in sentence format (nltk used)
    return finalMessage


# Plays the dank memer bot and saves a rod in case at risk
def sendDiscordFishsaver(browser, stringMessage, inputFeildXPATH):
    """
    :param browser:
    :param stringMessage:
    :param inputFeildXPATH:
    :return:
    """
    # Clicks on the input field, and types in the message to save rod
    time.sleep(5)
    sendmessage = browser.find_element_by_tag_name('body').send_keys(stringMessage + Keys.ENTER)
    print("sent : ", stringMessage)
    time.sleep(2)
    return 1


# Sends a message to the channel in the browser
def send(stringMessage, browser):
    """
    :param stringMessage: Message you wish to send to the browser through bot account
    :param browser: the broswer chrome instance
    :return: N/A
    """
    # Clicks on the input field, and types in the message
    clickIt = browser.find_element_by_xpath("//*[@class='form-2fGMdU']").click()
    time.sleep(1)

    sendmessage = browser.find_element_by_tag_name('body').send_keys(stringMessage + Keys.ENTER)
    print("sent + ", stringMessage)
    time.sleep(2)


# Clicks on an input field (Helper method)
def clickInputField(browser, inputFeildXPATH):
    """
    :param browser: Broswer instance
    :param inputFeildXPATH: XPATH of the input field
    :return: N/A
    """
    clickIt = browser.find_element_by_xpath(inputFeildXPATH).click()


# Parsing fishing commands and replying in the chat
def parseCommandAndRespond(browser, messageToWrite):
    print("Dank memer:", messageToWrite)
    if ("Type" in messageToWrite):
        print("fishing in progress..")
        messageToWrite = messageToWrite[::-1]
        if ("epyT" or "epyt" in messageToWrite):
            messageToWrite = messageToWrite[0:messageToWrite.index("epy") - 1]
            messageToWrite = messageToWrite[::-1]
        elif ("gnipyT" or "gnipyt" in messageToWrite):
            messageToWrite = messageToWrite[0:messageToWrite.index("gnipy") - 1]
            messageToWrite = messageToWrite[::-1]
        yes = send(messageToWrite, browser)
        time.sleep(30)  # Message cooldown in channel


# Post Meme command
def pmCommand(browser, numF):
    if numF % 3 == 0:
        send("pls pm", browser)
        time.sleep(4)
        if (numF % 2 == 0):
            send("d", browser)
        elif (numF % 3 == 0):
            send("e", browser)
        else:
            send("r", browser)


# Hunting command handler
def huntCommand(browser, messageToWrite):
    if ("Type" in messageToWrite):
        print("Hunting in progress..")
        #     print("\n\n Message to write: \n\n", messageToWrite)
        messageToWrite = messageToWrite[::-1]
        #     print("\n\n Message to write: \n\n", messageToWrite)
        if ("epyT" or "epyt" in messageToWrite):
            messageToWrite = messageToWrite[0:messageToWrite.index("epy") - 1]
            messageToWrite = messageToWrite[::-1]
        elif ("gnipyT" or "gnipyt" in messageToWrite):
            messageToWrite = messageToWrite[0:messageToWrite.index("gnipy") - 1]
            messageToWrite = messageToWrite[::-1]
        #     messageToWrite = messageToWrite[messageToWrite.index("T")+5:]
        yes = send(messageToWrite, browser)
        time.sleep(1)


# Handle begging commands
def plsBegCommand(browser, messageToWrite):
    if ("Type" in messageToWrite):
        print("Hunting in progress..")
        #     print("\n\n Message to write: \n\n", messageToWrite)
        messageToWrite = messageToWrite[::-1]
        #     print("\n\n Message to write: \n\n", messageToWrite)
        if ("epyT" or "epyt" in messageToWrite):
            messageToWrite = messageToWrite[0:messageToWrite.index("epy") - 1]
            messageToWrite = messageToWrite[::-1]
        elif ("gnipyT" or "gnipyt" in messageToWrite):
            messageToWrite = messageToWrite[0:messageToWrite.index("gnipy") - 1]
            messageToWrite = messageToWrite[::-1]
        #     messageToWrite = messageToWrite[messageToWrite.index("T")+5:]
        yes = send(messageToWrite, browser)
        time.sleep(1)

# Sends collected items to bot for safekeeping
def sendItemsToBot(invNum, browser, inv):

    try:
        for x in range(1, invNum + 15):
            getinv = "pls inv 1"
            send(getinv, browser)
            time.sleep(2)
            inv = getLastMessage(browser, 1)
            print(inv)

            invlist = nltk.word_tokenize(inv)
            invlist = invlist[invlist.index("─") - 1:]

            for i in range(0, 5):
                qty1 = invlist[invlist.index("─") + 1]
                if ',' in qty1:
                    qty = qty1[:qty1.index(',')] + qty1[qty1.index(',') + 1:]
                    qty = int(qty)
                else:
                    qty = int(qty1)
                print(qty)
                item = invlist[invlist.index("─") + 3]
                if (item == "huntingrifle" or item == "lifesaver" or item == "fishingpole" or item == "laptop"):
                    print(item)
                    senditem = "pls dont gift " + str(qty) + " " + item + " trmp"
                    print(senditem)
                    invlist = invlist[invlist.index(item) + 2:]

                    continue
                print(item)
                senditem = "pls gift " + str(qty) + " " + item + " trmp"
                send(senditem, browser)
                invlist = invlist[invlist.index(item) + 2:]

                time.sleep(21)
    except:
        print("except.getMessage()")

#
#	MAIN LOGIC
#

def main():
    # Creating the browser instance
    browser = openDiscordAndLogin(USERNAME, PASS, CHANNEL_LINK, CHROME_DRIVER_LOCATION)
    # Wait for channel to load
    time.sleep(10)

    # Config settings
    numF = 0
    delay = 17
    time.sleep(10)
    numLoops = 500

    for i in range(0, numLoops):
        # Send command from bot
        send("pls fish", browser)
        time.sleep(1.6)
        numF += 1
        # Parsing fishing commands
        messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)
        parseCommandAndRespond(browser, messageToWrite)

        # Posting memes to channel command
        time.sleep(10)
        pmCommand(browser, numF)
        messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)
        parseCommandAndRespond(browser, messageToWrite)

        # Hunting command
        send("pls hunt", browser)
        messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)
        huntCommand(browser, messageToWrite)

        # Begging commands
        time.sleep(delay)
        send("pls beg", browser)
        messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)
        plsBegCommand(browser, messageToWrite)

        time.sleep(10)

    print(numF)

    # Send items collected to the other account or a bot for safekeeping and storage
    send("pls inv", browser)
    time.sleep(3)
    inv = getLastMessage(browser, 1)
    print(inv)
    time.sleep(2)
    invNum = int(inv[-1:])

    sendItemsToBot(invNum, browser, inv)



main()
