#Functions for the production of hydrogen gas and polymer mix in the liquid CH4 moderators
import pandas as pd

def Mod_Data_Reader(path):
    
    df = pd.read_csv(path)
    df.drop(['Unnamed: 0'], axis = 1, inplace = True)
    
    return(df)


def moles_per_MGy_per_g(G_value):
    '''
        first finds moles per g of CH4 for 1 Gy
        then returns moles for 1MGy per g of CH4
    '''
    
    moles_per_g = G_value/1000    #since 1Gy = 1J/kg
    moles_per_MGy_per_g = moles_per_g * 1e6 
    
    return(moles_per_MGy_per_g)


def radicals_per_MGy_per_g(moles_per_MGy_per_g):
    'This finds the number of radicals per MGy per g of CH4'
    
    rads_per_dose = moles_per_MGy_per_g * 6.023e23
    
    return(rads_per_dose)



def vol_of_H_per_s(moles_per_MGy_per_g, CH4_vol, dose_rate, SG):
    '''
        Evans paper method - SG is specific gravity, in this case its essentially used as density
        This finds the volume of H gas per MGy per g of CH4
        Then returns the volume of H per s for a known dose rate(MGy/s) and volume of CH4(cm3)
    '''
    STP_vol = moles_per_MGy_per_g * 2.24e4
    
    h_produced = STP_vol * CH4_vol * SG * dose_rate
    
    return(h_produced)


#def g_val_conversion(G_value):
    #' These foolowing 3 do the H production rate with a different method'
    
    #new_G_val = G_value * (6.023e23/6.242e12)
    
    #return(new_G_val)
    


#def dose_rate_conversion(dose, mass_CH4):
    
    #new_dose_rate = dose * mass_CH4 * 6.242e18
    
    #return(new_dose_rate)



#def vol_of_H_b(new_dose, new_g_value):
    
    #h_production = (new_dose * new_g_value * 2.24e4)/ 6.023e23
    
    #return(h_production)


def molecular_weight(n):
    ' returns the molecular weight of the polymer (CH2)n for a chain length n '
    mr = (12 + 2) * n 
    
    return (mr)



def rate_of_pol_form(G_value, mr, dose_rate, mass_CH4):
    '''
        First finds the polymer produced per MGy per g of CH4
        Then returns the polymer production per second for a known dose (MGy) and mass of CH4 (g)
    '''
    
    polymer_form_per_dose = moles_per_MGy_per_g(G_value) * mr
    
    polymer_per_sec = polymer_form_per_dose * dose_rate * mass_CH4
    
    return(polymer_per_sec)    


def MeV_per_g_per_sec_to_MGy_per_sec(value):
    ' This converts the rate of energy absorption per g (MeV/g/s) to the absorbed dose rate (MGy/s)'
    
    dose_rate = value * 1.60218E-16
    
    return(dose_rate)