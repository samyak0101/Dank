
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

print("KAMLESH HAS STARTED SUCCESSFULLY")
time.sleep(5)

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
# # op.add_argument("--disable-gpu")

browser = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

channelLink = "https://discord.com/channels/763624613426102322/775289257220374549"

#
#	METHOD DECLARATIONS
#


def getLastMessage(browser, num):
    messageMegaBox = browser.find_element_by_xpath("//div[@class='scrollerInner-2YIMLh']").text
    # print(messageMegaBox)
    messageSentences = nltk.sent_tokenize(messageMegaBox)

    # print("message sentences = ", messageSentences)

    # print(nltk.word_tokenize(messageSentences[-1]))
    lastSentences = messageSentences[-5] + messageSentences[-4] + messageSentences[-3] + messageSentences[-2] + messageSentences[-1]
    # print("last 5 sentences from getmessages\n", lastSentences)
    subFinalMessage =  nltk.word_tokenize(lastSentences)
#     print("\n\n\n\n",lastSentences)
    # print("\n\n\n\n\n\n\n\n\n",subFinalMessage, "\n\n\n\n\n\n\n\n\n")
    #     subFinalMessage = subFinalMessage[::-1]
    #     mostRecentMessage = subFinalMessage.index("ta yadoT")

    #####
    # print(nltk.word_tokenize(""))
    subFinalMessage = subFinalMessage[::-1]
#     print("This is the subfinalmessage before searching for Today: \n\n\n" , subFinalMessage)
    finalMessage = subFinalMessage[0:subFinalMessage.index("Today")]
    
    if(num==1):
        finalMessage = subFinalMessage[0:subFinalMessage.index("BOT")]
        finalMessage = finalMessage[::-1]
        finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[4:])
        if(finalMessage == "pause"):
            send("pausing for 60 second", browser)
            time.sleep(60)
        return finalMessage

    if(subFinalMessage.index("BOT")<subFinalMessage.index("SamyToday")):
#         print("bot index found first bro")
        finalMessage = subFinalMessage[0:subFinalMessage.index("BOT")]
        finalMessage = finalMessage[::-1]
        finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[4:])
        print("Dank Memer: ", finalMessage)
        return "bot"

    elif(subFinalMessage.index("BOT")>subFinalMessage.index("SamyToday")):
#         print("samy index found first bro")
        finalMessage = subFinalMessage[0:subFinalMessage.index("SamyToday")]
        finalMessage = finalMessage[::-1]
        finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[3:])
        print("Samy: ", finalMessage)

        return "samy"




def getNumMessages(browser, messageContainerXPATH, numMessages):
	#Navigates to the messageBox and stores the messages requested by user
	messageMegaBox = browser.find_element_by_xpath(messageContainerXPATH).text
	messageSentences = nltk.sent_tokenize(messageMegaBox)
	# print(messageSentences)
	lastSentences = messageSentences[-12] + messageSentences[-11] + messageSentences[-10] + messageSentences[-9] + messageSentences[-8] + messageSentences[-7] + messageSentences[-6] + messageSentences[-5] + messageSentences[-4] + messageSentences[-3] + messageSentences[-2] + messageSentences[-1]
	print("last 5 sentences from getmessages\n", lastSentences)
	subFinalMessage =  nltk.word_tokenize(lastSentences)
	subFinalMessage = subFinalMessage[::-1]
	# print("This is the subfinalmessage before searching for Today: \n\n\n" , subFinalMessage)
	finalMessage = subFinalMessage[0:subFinalMessage.index("Today")]
	finalMessage = finalMessage[::-1]
	# while "-r" or "resume" not in finalMessage:
	# 	if ("-p" or "pause" in finalMessage):
	# 		time.sleep(15)
	# 		messageMegaBox = browser.find_element_by_xpath(messageContainerXPATH).text
	# 		messageSentences = nltk.sent_tokenize(messageMegaBox)
	#         # print(messageSentences)
	#         lastSentences = messageSentences[-5] + messageSentences[-4] + messageSentences[-3] + messageSentences[-2] + messageSentences[-1]
	#         # print(lastSentences)
	#         subFinalMessage =  nltk.word_tokenize(lastSentences)
	#         subFinalMessage = subFinalMessage[::-1]
	#         # print("This is the subfinalmessage before searching for Today: \n\n\n" , subFinalMessage)
	#         finalMessage = subFinalMessage[0:subFinalMessage.index("Today")]
	#         finalMessage = finalMessage[::-1]

            
	finalMessage = TreebankWordDetokenizer().detokenize(finalMessage[3:])
	#returns stored messages in sentence format (nltk used)
	return finalMessage

def sendDiscordFishsaver(browser, stringMessage, inputFeildXPATH):
	#Clicks on the input feild, and types in the message
	time.sleep(1)

	sendmessage = browser.find_element_by_tag_name('body').send_keys(stringMessage + Keys.ENTER)
	print("sent : ", stringMessage)
	time.sleep(2)
	return 1
	#returns boolean value (yes if printed correctly, no if twas an error)

def send(stringMessage, browser):
	#Clicks on the input feild, and types in the message
	clickIt = browser.find_element_by_xpath("//*[@class='form-2fGMdU']").click()
	time.sleep(1)

	sendmessage = browser.find_element_by_tag_name('body').send_keys(stringMessage + Keys.ENTER)
	print("sent + ", stringMessage)
	# time.sleep(2)
	return 1
	#returns boolean value (yes if printed correctly, no if twas an error)

def closeInstances ():
	#Closes everything
	return 1

def clickInputField(browser, inputFeildXPATH):
    clickIt = browser.find_element_by_xpath(inputFeildXPATH).click()
    return (1)

#VARIABLE DECLARATIONS







USERNAME = "javi.erfr.anc.i.sco.tm.p@gmail.com"
PASS = "Samyakjain101"
try:

	enterUsername = browser.find_element_by_css_selector("[type=text]")
	enterUsername.send_keys(USERNAME)
	enterUsername.send_keys(Keys.TAB)
	
except:
	enterUsername = browser.find_element_by_css_selector("[type=email]")
	enterUsername.send_keys(USERNAME)
	enterUsername.send_keys(Keys.TAB)

enterPassword = browser.find_element_by_css_selector("[type=password]")
enterPassword.send_keys(PASS)
enterPassword.send_keys(Keys.ENTER)

time.sleep(5)
browser.get(channelLink)
time.sleep(5)
#
#	MAIN LOGIC AND METHOD
#

time.sleep(10)


numFishies = 0
delay = 17
time.sleep(10);
send("I am great. I am awesome. Today is my day. Today I will  grind so much for Samy. Today I will wreak havoc. Today I will make my master RICH. He deserves to be ultra rich. I will take it headon. Praise today. Amen. Samy ji Jai. I am gr8. I am even gr8ier. I am gr9iest. Ok done i think this is enough messages.\npls beg", browser)


for i in range (0,500):

# send("pls bet 420", browser)
# time.sleep(1.5)

	send("pls fish", browser)
	time.sleep(1.6)
	numFishies+=1


	messageToWrite =  getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)
	print("Dank memer:", messageToWrite)
	if ("Type" in messageToWrite):
	    print("fishing in progress..")
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    messageToWrite = messageToWrite[::-1]
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    if("epyT" or "epyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("epy")-1]
	        messageToWrite = messageToWrite[::-1]
	    elif("gnipyT" or "gnipyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("gnipy")-1]
	        messageToWrite = messageToWrite[::-1]
	#     messageToWrite = messageToWrite[messageToWrite.index("T")+5:]
	    yes = send(messageToWrite, browser)
	    time.sleep(35)




	time.sleep(10)
	if numFishies%3==0:
	    send("pls pm", browser)
	    time.sleep(4)
	    if (numFishies%2==0):
	        send("d", browser)
	    elif(numFishies%3==0):
	        send("e", browser)
	    else:
	        send("r", browser)
	print("sleeping now")


	time.sleep(1)
	messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)
	if ("Type" in messageToWrite):
	    print("fishing in progress..")
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    messageToWrite = messageToWrite[::-1]
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    if("epyT" or "epyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("epy")-1]
	        messageToWrite = messageToWrite[::-1]
	    elif("gnipyT" or "gnipyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("gnipy")-1]
	        messageToWrite = messageToWrite[::-1]
	#     messageToWrite = messageToWrite[messageToWrite.index("T")+5:]
	    yes = send(messageToWrite, browser)
	    time.sleep(1)


	send("pls hunt", browser)
	print("starting parse + reply now:")
	time.sleep(1.5)
	
	messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)

	if ("Type" in messageToWrite):
	    print("fishing in progress..")
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    messageToWrite = messageToWrite[::-1]
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    if("epyT" or "epyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("epy")-1]
	        messageToWrite = messageToWrite[::-1]
	    elif("gnipyT" or "gnipyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("gnipy")-1]
	        messageToWrite = messageToWrite[::-1]
	#     messageToWrite = messageToWrite[messageToWrite.index("T")+5:]
	    yes = send(messageToWrite, browser)
	    time.sleep(1)

	print("parse process over")

	time.sleep(5+delay)
	send("pls beg", browser)

	time.sleep(1)
	messageToWrite = getNumMessages(browser, "//div[@class='scrollerInner-2YIMLh']", 1)

	if ("Type" in messageToWrite):
	    print("fishing in progress..")
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    messageToWrite = messageToWrite[::-1]
	#     print("\n\n Message to write: \n\n", messageToWrite)
	    if("epyT" or "epyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("epy")-1]
	        messageToWrite = messageToWrite[::-1]
	    elif("gnipyT" or "gnipyt" in messageToWrite):
	        messageToWrite = messageToWrite[0:messageToWrite.index("gnipy")-1]
	        messageToWrite = messageToWrite[::-1]
	#     messageToWrite = messageToWrite[messageToWrite.index("T")+5:]
	    yes = send(messageToWrite, browser)
	    time.sleep(1)

	time.sleep(10)
	print("fished already these many times: ", numFishies)

print("done")
print(numFishies)



send("pls inv", browser)
time.sleep(3)
inv = getLastMessage(browser, 1)
print(inv)
time.sleep(2)
invNum = int(inv[-1:])

try:
    for x in range (1,invNum+15):
        getinv = "pls inv 1"
        send(getinv, browser)
        time.sleep(2)
        inv = getLastMessage(browser, 1)
        print(inv)

        invlist = nltk.word_tokenize(inv)
        invlist = invlist[invlist.index("─")-1:]

        for i in range (0,5):
            qty1 = invlist[invlist.index("─")+1]
            if ',' in qty1:
                qty = qty1[:qty1.index(',')] + qty1[qty1.index(',')+1:]
                qty = int(qty)
            else:
                qty = int(qty1)
            print(qty)
            item = invlist[invlist.index("─")+3]
            if(item=="huntingrifle" or item =="lifesaver" or item =="fishingpole" or item =="laptop"):
                print(item)
                senditem = "pls dont gift "+str(qty)+" "+item+" trmp"
                print(senditem)
                invlist = invlist[invlist.index(item)+2:]

                continue
            print(item)
            senditem = "pls gift "+str(qty)+" "+item+" trmp"
            send(senditem, browser)
            invlist = invlist[invlist.index(item)+2:]

            time.sleep(21)
except:
    print("except.getMessage()")
