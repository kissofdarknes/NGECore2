import sys
from services.spawn import MobileTemplate
from services.spawn import WeaponTemplate
from java.util import Vector

def addTemplate(core):
	mobileTemplate = MobileTemplate()	
	
	mobileTemplate.setCreatureName('minor_sludge_panther')
	mobileTemplate.setLevel(37)
	mobileTemplate.setDifficulty(0)
	mobileTemplate.setAttackRange(5)
	mobileTemplate.setAttackSpeed(1.0)
	mobileTemplate.setWeaponType(6)
	mobileTemplate.setMinSpawnDistance(5)
	mobileTemplate.setMaxSpawnDistance(10)
	mobileTemplate.setDeathblow(False)
	mobileTemplate.setScale(.7)
	mobileTemplate.setMeatType("Carnivore Meat")
	mobileTemplate.setMeatAmount(20)
	mobileTemplate.setHideType("Leathery Hide")
	mobileTemplate.setBoneAmount(27)	
	mobileTemplate.setBoneType("Mammal Bone")
	mobileTemplate.setHideAmount(27)
	mobileTemplate.setSocialGroup("sludge panther")
	mobileTemplate.setAssistRange(6)
	mobileTemplate.setStalker(False)
	mobileTemplate.setOptionsBitmask(192)	

	templates = Vector()
	templates.add('object/mobile/shared_sludge_panther.iff')
	mobileTemplate.setTemplates(templates)

	weaponTemplates = Vector()
	weapontemplate = WeaponTemplate('object/weapon/melee/unarmed/shared_unarmed_default.iff', 6, 1.0)
	weaponTemplates.add(weapontemplate)
	mobileTemplate.setWeaponTemplateVector(weaponTemplates)

	attacks = Vector()
	mobileTemplate.setDefaultAttack('creatureMeleeAttack')
	mobileTemplate.setAttacks(attacks)

	core.spawnService.addMobileTemplate('minor_sludge_panther', mobileTemplate)
	return