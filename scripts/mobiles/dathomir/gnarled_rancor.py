import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from resources.datatables import WeaponType
from resources.datatables import Difficulty
from resources.datatables import Options
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()
	
	mobileTemplate.setCreatureName('gnarled_rancor')
	mobileTemplate.setLevel(78)
	mobileTemplate.setDifficulty(Difficulty.ELITE)
	mobileTemplate.setMinSpawnDistance(4)
	mobileTemplate.setMaxSpawnDistance(8)
	mobileTemplate.setDeathblow(True)
	mobileTemplate.setScale(1)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(950)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setHideAmount(876)
	mobileTemplate.setBoneType("Animal Bones")
	mobileTemplate.setBoneAmount(776)
	mobileTemplate.setSocialGroup("rancor")
	mobileTemplate.setAssistRange(12)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(Options.AGGRESSIVE | Options.ATTACKABLE)
	
	templates = Vector()
	templates.add('object/mobile/shared_rancor.iff')
	mobileTemplate.setTemplates(templates)
	
	
	attacks = Vector()
	attacks.add('bm_dampen_pain_5')
	attacks.add('bm_shaken_3')
	attacks.add('bm_stomp_5')
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)
	
	core.spawnService.addMobileTemplate('gnarled_rancor', mobileTemplate)