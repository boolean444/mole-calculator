from molecule import get_molarmass

avogadro = 6.02 * 10**23

def atom_mole(atoms=0, moles=0):
    if atoms:
        return atoms / avogadro
    else:
        return moles * avogadro

def atom_gram(molecule, atoms=0, grams=0): # molecule is optional
    if atoms:
        molar = get_molarmass(molecule)
        return atom_mole(atoms=atoms) * molar
    else:
        return atom_mole(moles=mole_gram(molecule=molecule, grams=grams)) # gram => mole => atom

def mole_gram(molecule, moles=0, grams=0):
    molar = get_molarmass(molecule)
    if moles:
        return moles * molar
    else:
        return grams / molar


def give_conversion(item1, item2):
    if item1 == item2:
        return lambda **kwargs: list(kwargs.values())[0] # returns the value of the input
    elif item1 == "moles" or item2 == "moles":
        if item1 == "atoms" or item2 == "atoms":
            return atom_mole
        if item1 == "grams" or item2 == "grams":
            return mole_gram
    else:
        return atom_gram