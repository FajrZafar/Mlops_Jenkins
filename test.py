from main import Bulb


bulb=Bulb()
def test_bulb_isOff():
    assert bulb.getstatus()=="Bulb id not glowing"
    

def test_bulb_isOn():
    bulb.ison()
    assert bulb.getstatus()=="Bulb is glowing"
    
def test_getStatus():
     bulb.isOff()
     assert bulb.getstatus()=="Bulb is not glowing"

def test_toggle_bulb_state():
    # Initially, the bulb should be off
    assert bulb.getstatus() == "Bulb is not glowing"
    
    # Turn on the bulb
    bulb.ison()
    assert bulb.getstatus() == "Bulb is glowing"
    
    # Toggle the bulb state
    bulb.toggle()
    assert bulb.getstatus() == "Bulb is not glowing"  # The state should be off after toggling
    
    # Toggle again
    bulb.toggle()
    assert bulb.getstatus() == "Bulb is glowing"  # The state should be on after toggling

