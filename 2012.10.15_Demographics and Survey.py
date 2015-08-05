#!/usr/bin/env python

#------------------------------------------------------------------------------------ Demographics and Survey ------------------------------------------------------------------------------------

# The completion time is the difference between the time when the ratings are first presented and the time when the ratings disappear.

from psychopy import visual, gui, sys, core, event
 
# Basic experimenter and participant info.
myDlg = gui.Dlg(title = 'DEMOGRAPHIC INFORMATION FORM')
myDlg.addText('Experiment Name: Visual Perception and Search')
myDlg.addField('Participant Number: ', '999')
myDlg.addText('Basic Information:')
myDlg.addField('Age: ', '999')
myDlg.addField('Gender:',choices = ['Male', 'Female'])
myDlg.addField('Number of years of education completed: ', '999')
myDlg.addField('Handedness: ',choices = ['Right-Handed', 'Left-Handed'])
myDlg.addField('Do you have normal or corrected-to-normal vision?',choices = ['Yes', 'No'])
myDlg.addField('Are you color-blind?',choices = ['Yes', 'No', 'Not Sure'])
myDlg.show()
if myDlg.OK:
    myDlgData = myDlg.data
else:
    sys.exit()
    
	
# Create output file.
myOutFileName = 'BIS_BAS_' + myDlgData[1] + '_' + myDlgData[0] + '.txt'
myOutFile = open(myOutFileName, 'w')

# Create window.
myWin = visual.Window(fullscr = True, monitor = 'testMonitor', rgb = [1, 1, 1])
    
# Variables for all scales.
sizefactorC = .4
hstretchC = 2
itemheightC = .04
responsesC = ['1             ', '         2              ', '        3          ', '            4']

# Title and instructions
myBISBASTitle1 = visual.TextStim(myWin, text = "BIS/BAS Inventory (Page 1)", height = .05, color = 'Black', pos = (0, .9))
myBISBASInst1 = visual.TextStim(myWin, text = "For each statement, please click the number in the column that best indicates how much you agree or disagree with what the statement says.  WHEN COMPLETED, PRESS ENTER AT LEAST 12 TIMES.", height = .04, color = 'Black', pos = (0, .8))
myBISBASTitle2 = visual.TextStim(myWin, text = "BIS/BAS Inventory (Page 2)", height = .05, color = 'Black', pos = (0, .9))
myBISBASInst2 = visual.TextStim(myWin, text = "For each statement, please click the number in the column that best indicates how much you agree or disagree with what the statement says.  WHEN COMPLETED, PRESS ENTER AT LEAST 12 TIMES.", height = .04, color = 'Black', pos = (0, .8))

# Rating descriptions
myDescription0 = visual.TextStim(myWin, text = "Very true\nfor me", height = .03, color = 'Black', pos = (.16, .6))
myDescription1 = visual.TextStim(myWin, text = "Somewhat true\nfor me", height = .03, color = 'Black', pos = (.31, .6))
myDescription2 = visual.TextStim(myWin, text = "Somewhat false\nfor me", height = .03, color = 'Black', pos = (.48, .6))
myDescription3 = visual.TextStim(myWin, text = "Very false\nfor me", height = .03, color = 'Black', pos = (.64, .6))

# 1. A person's family is the...
myFamily_Item = visual.TextStim(myWin, text = "A person's family is the most important thing in life.", height = itemheightC, color = 'Black', pos = (-.4, .4))
myFamily = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .4), showAccept = False) 
    
# 2. Even if something bad...
myBad_Item = visual.TextStim(myWin, text = "Even if something bad is about to happen to me, I rarely experience fear or nervousness.", height = itemheightC, color = 'Black', pos = (-.4, .3))
myBad = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .3), showAccept = False) 
    
# 3. I go out of my way...
myWay_Item = visual.TextStim(myWin, text = "I go out of my way to get things I want.", height = itemheightC, color = 'Black', pos = (-.4, .2))
myWay = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .2), showAccept = False)
    
# 4. When I'm doing well...
myWell_Item = visual.TextStim(myWin, text = "When I'm doing well at something, I love to keep at it.", height = itemheightC, color = 'Black', pos = (-.4, .1))
myWell = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .1), showAccept = False)
    
# 5. I'm always willing to...
myWilling_Item = visual.TextStim(myWin, text = "I'm always willing to try something new if I think it will be fun.", height = itemheightC, color = 'Black', pos = (-.4, 0))
myWilling = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, 0), showAccept = False)
    
# 6. How I dress is...
myDress_Item = visual.TextStim(myWin, text = "How I dress is important to me.", height = itemheightC, color = 'Black', pos = (-.4, -.1))
myDress = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.1), showAccept = False)
    
# 7. When I get something...
myGet_Item = visual.TextStim(myWin, text = "When I get something I want, I feel excited and energized.", height = itemheightC, color = 'Black', pos = (-.4, -.2))
myGet = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.2), showAccept = False)
    
# 8. Criticism or scolding...
myScolding_Item = visual.TextStim(myWin, text = "Criticism or scolding hurts me quite a bit.", height = itemheightC, color = 'Black', pos = (-.4, -.3))
myScolding = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.3), showAccept = False)
    
# 9. When I want something...
myWant_Item = visual.TextStim(myWin, text = "When I want something I usually go all-out to get it.", height = itemheightC, color = 'Black', pos = (-.4, -.4))
myWant = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.4), showAccept = False)
    
# 10. I will often do things...
myOften_Item = visual.TextStim(myWin, text = "I will often do things for no other reason than that they might be fun.", height = itemheightC, color = 'Black', pos = (-.4, -.5))
myOften = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.5), showAccept = False)
    
# 11. It's hard for me to find...
myHard_Item = visual.TextStim(myWin, text = "It's hard for me to find the time to do things such as get a haircut.", height = itemheightC, color = 'Black', pos = (-.4, -.6))
myHard = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.6), showAccept = False)
    
# 12. If I see a chance...
myChance_Item = visual.TextStim(myWin, text = "If I see a chance to get something I want I move on it right away.", height = itemheightC, color = 'Black', pos = (-.4, -.7))
myChance = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.7), showAccept = False)
    
# 13. I feel pretty worried...
myWorried_Item = visual.TextStim(myWin, text = "I feel pretty worried or upset when I think or know somebody is angry at me.", height = itemheightC, color = 'Black', pos = (-.4, .4))
myWorried = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .4), showAccept = False)
    
# 14. When I see an opportunity...
myOpportunity_Item = visual.TextStim(myWin, text = "When I see an opportunity for something I like I get excited right away.", height = itemheightC, color = 'Black', pos = (-.4, .3))
myOpportunity = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .3), showAccept = False)
    
# 15. I often act... 
myAct_Item = visual.TextStim(myWin, text = "I often act on the spur of the moment.", height = itemheightC, color = 'Black', pos = (-.4, .2))
myAct = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .2), showAccept = False)
    
# 16. If I think something...
myThink_Item = visual.TextStim(myWin, text = "If I think something unpleasant is going to happen I usually get pretty 'worked up'.", height = itemheightC, color = 'Black', pos = (-.4, .1))
myThink = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, .1), showAccept = False)
    
# 17. I often wonder why...
myWonder_Item = visual.TextStim(myWin, text = "I often wonder why people act the way they do.", height = itemheightC, color = 'Black', pos = (-.4, 0))
myWonder = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, 0), showAccept = False)
    
# 18. When good things happen...
myGood_Item = visual.TextStim(myWin, text = "When good things happen to me, it affects me strongly.", height = itemheightC, color = 'Black', pos = (-.4, -.1))
myGood = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.1), showAccept = False)
    
# 19. I feel worried...
myFeel_Item = visual.TextStim(myWin, text = "I feel worried when I think I have done poorly at something important.", height = itemheightC, color = 'Black', pos = (-.4, -.2))
myFeel = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.2), showAccept = False)
    
# 20. I crave excitement...
myCrave_Item = visual.TextStim(myWin, text = "I crave excitement and new sensations.", height = itemheightC, color = 'Black', pos = (-.4, -.3))
myCrave = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.3), showAccept = False)

# 21. When I go after...
myAfter_Item = visual.TextStim(myWin, text = "When I go after something I use a 'no holds barred' approach.", height = itemheightC, color = 'Black', pos = (-.4, -.4))
myAfter = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.4), showAccept = False)	

# 22. I have very few fears...
myFears_Item = visual.TextStim(myWin, text = "I have very few fears compared to my friends.", height = itemheightC, color = 'Black', pos = (-.4, -.5))
myFears = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.5), showAccept = False)	

# 23. It would excite me...
myExcite_Item = visual.TextStim(myWin, text = "It would excite me to win a contest.", height = itemheightC, color = 'Black', pos = (-.4, -.6))
myExcite = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.6), showAccept = False)

# 24. I worry about making...
myMaking_Item = visual.TextStim(myWin, text = "I worry about making mistakes.", height = itemheightC, color = 'Black', pos = (-.4, -.7))
myMaking = visual.RatingScale(myWin, choices = responsesC, lineColor = 'Black', textColor = 'Black', \
    stretchHoriz = hstretchC, displaySizeFactor = sizefactorC, showValue = False, pos = (.4, -.7), showAccept = False)

# Create clock for taking the time to complete the questionnaire.
myClock = core.Clock()

# Grab the starting time.
myStartTime = myClock.getTime()

# Draw objects for Page 1.
while myFamily.noResponse or myBad.noResponse or myWay.noResponse or myWell.noResponse or myWilling.noResponse or myDress.noResponse or myGet.noResponse or myScolding.noResponse or myWant.noResponse or myOften.noResponse or myHard.noResponse or myChance.noResponse:
    myBISBASTitle1.draw()
    myBISBASInst1.draw()
    myDescription0.draw()
    myDescription1.draw()
    myDescription2.draw()
    myDescription3.draw()
    myFamily.draw()
    myFamily_Item.draw()
    myBad.draw()
    myBad_Item.draw()
    myWay.draw()
    myWay_Item.draw()
    myWell.draw()
    myWell_Item.draw()
    myWilling.draw()
    myWilling_Item.draw()
    myDress.draw()
    myDress_Item.draw()
    myGet.draw()
    myGet_Item.draw()
    myScolding.draw()
    myScolding_Item.draw()
    myWant.draw()
    myWant_Item.draw()
    myOften.draw()
    myOften_Item.draw()
    myHard.draw()
    myHard_Item.draw()
    myChance.draw()
    myChance_Item.draw()
    myWin.flip()
    
# Refresh screen for second page.
myWin.flip()

# Draw objects for Page 2.
while myWorried.noResponse or myOpportunity.noResponse or myAct.noResponse or myThink.noResponse or myWonder.noResponse or myGood.noResponse or myFeel.noResponse or myCrave.noResponse or myAfter.noResponse or myFears.noResponse or myExcite.noResponse or myMaking.noResponse:
    myBISBASTitle2.draw()
    myBISBASInst2.draw()
    myDescription0.draw()
    myDescription1.draw()
    myDescription2.draw()
    myDescription3.draw()
    myWorried.draw()
    myWorried_Item.draw()
    myOpportunity.draw()
    myOpportunity_Item.draw()
    myAct.draw()
    myAct_Item.draw()
    myThink.draw()
    myThink_Item.draw()
    myWonder.draw()
    myWonder_Item.draw()
    myGood.draw()
    myGood_Item.draw()
    myFeel.draw()
    myFeel_Item.draw()
    myCrave.draw()
    myCrave_Item.draw()
    myAfter.draw()
    myAfter_Item.draw()
    myFears.draw()
    myFears_Item.draw()
    myExcite.draw()
    myExcite_Item.draw()
    myMaking.draw()
    myMaking_Item.draw()
    myWin.flip()
    

# Grab the end time.
myEndTime = myClock.getTime()

# Calculate completion time.
myCompletionTime = myEndTime - myStartTime

# Convert to string for printing.
myFamilyRating = str(myFamily.getRating())
myBadRating = str(myBad.getRating())
myWayRating = str(myWay.getRating())
myWellRating = str(myWell.getRating())
myWillingRating = str(myWilling.getRating())
myDressRating = str(myDress.getRating())
myGetRating = str(myGet.getRating())
myScoldingRating = str(myScolding.getRating())
myWantRating = str(myWant.getRating())
myOftenRating = str(myOften.getRating())
myHardRating = str(myHard.getRating())
myChanceRating = str(myChance.getRating())
myWorriedRating = str(myWorried.getRating())
myOpportunityRating = str(myOpportunity.getRating())
myActRating = str(myAct.getRating())
myThinkRating = str(myThink.getRating())
myWonderRating = str(myWonder.getRating())
myGoodRating = str(myGood.getRating())
myFeelRating = str(myFeel.getRating())
myCraveRating = str(myCrave.getRating())
myAfterRating = str(myAfter.getRating())
myFearsRating = str(myFears.getRating())
myExciteRating = str(myExcite.getRating())
myMakingRating = str(myMaking.getRating())
myStartTimeStr = str(myStartTime)
myEndTimeStr = str(myEndTime)
myCompletionTimeStr = str(myCompletionTime)

# Print experimenter and participant info to output file.
myOutFile.write('Participant Number:\t' + myDlgData[0] + '\n' + 'Age:\t' + myDlgData[1] + '\n' + 'Gender:\t' + myDlgData[2] + '\n' + 'Number of years of education completed:\t' + myDlgData[3] + '\n' + 'Handedness:\t' + myDlgData[4] + '\n' + 'Do you have normal or corrected-to-normal vision?:\t' + myDlgData[5] + '\n' + 'Are you color-blind?:\t' + myDlgData[6] + '\n')

# Print start, end, and completion times.
myOutFile.write('Start time(sec):\t' + myStartTimeStr + '\n' + 'End time(sec):\t' + myEndTimeStr + '\n' + 'Completion Time(sec):\t' + myCompletionTimeStr + '\n\n')

# Print column headings.
myOutFile.write('1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\n')

# Print user responses.
myOutFile.write(myFamilyRating + '\t' + myBadRating + '\t' + myWayRating + '\t' + myWellRating + '\t' + myWillingRating + '\t' + myDressRating + '\t' + 
    myGetRating + '\t' + myScoldingRating + '\t' + myWantRating + '\t' + myOftenRating + '\t' + myHardRating + '\t' + myChanceRating + '\t' + myWorriedRating + '\t' + myOpportunityRating + '\t' + 
    myActRating + '\t' + myThinkRating + '\t' + myWonderRating + '\t' + myGoodRating + '\t' + myFeelRating + '\t' + myCraveRating  + '\t' + myAfterRating + '\t' + myFearsRating + '\t' + myExciteRating + '\t' + myMakingRating + '\n') 
