### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # comparators use double equal ==
      return True
    else    # missing (:)
      return False
   

  dif highest_card(self, card1 card2): #spelling def and the coma after card1.
  if card1.value > card2.value: # identation is wrong for lines 28 - 31.
    return card # we need to return card1. 
  else:
    return card2
  


def cards_total(self, cards): #identation
  total  #we need the initial value of the variable, usually zero. 
  for card in cards:
    total += card.value
    return "You have a total of" + total #return is inside the for loop and should be outside. Must return total as a number, not a string
  
```
