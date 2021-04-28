import json
import primer3 #will have to pip install primer3-py
import sys

def primerscore(filename):
    primer_names = []
    primer_scores = []
    output = open(filename, 'r')
    outputdata = json.load(output) #load json data from repp output
    for field in outputdata['solutions'][0]['fragments']:
        if 'primers' in field.keys():
            primerlist = field['primers']
            for prim in primerlist:
                primer = prim['seq'] #set to each outputted primer from repp
                primerlength = len(primer)
                melting = primer3.calcTm(primer) #would not use tm from repp as values differ slightly from primer3
                homodimer = primer3.calcHomodimer(primer)
                gcpercent = prim['gc'] #retain from repp output
                annealingtemp = melting - 5
                hairpin = primer3.calcHairpin(primer)
                #begin scoring each primer

                if((primerlength > 17) and (primerlength < 23)):
                    lengthscore = 10
                elif((primerlength > 16) and (primerlength < 24)):
                    lengthscore = 9
                elif((primerlength > 15) and (primerlength < 25)):
                    lengthscore = 8
                elif((primerlength > 14) and (primerlength < 26)):
                    lengthscore = 7
                elif((primerlength > 13) and (primerlength < 27)):
                    lengthscore = 6
                elif((primerlength > 12) and (primerlength < 28)):
                    lengthscore = 5
                elif((primerlength > 11) and (primerlength < 29)):
                    lengthscore = 4
                elif((primerlength > 10) and (primerlength < 30)):
                    lengthscore = 3
                elif((primerlength > 9) and (primerlength < 31)):
                    lengthscore = 2
                elif((primerlength <= 9) or (primerlength >= 31)):
                    lengthscore = 1

                if((melting > 50) and (melting < 58)):
                    mprimerscore = 10
                elif((melting > 48) and (melting < 60)):
                    mprimerscore = 9
                elif((melting > 46) and (melting < 62)):
                    mprimerscore = 8
                elif((melting > 44) and (melting < 64)):
                    mprimerscore = 7
                elif((melting > 42) and (melting < 66)):
                    mprimerscore = 6
                elif((melting > 40) and (melting < 68)):
                    mprimerscore = 5
                elif((melting > 38) and (melting < 70)):
                    mprimerscore = 4
                elif((melting > 36) and (melting < 72)):
                    mprimerscore = 3
                elif((melting > 34) and (melting < 74)):
                    mprimerscore = 2
                elif((melting <= 34) or (melting >= 60)):
                    mprimerscore = 1

                if(homodimer.structure_found == False):
                    hdimerscore = 10
                elif((homodimer.structure_found == True) and (homodimer.dg > -1500)):
                    hdimerscore = 9
                elif((homodimer.structure_found == True) and (homodimer.dg > -3000)):
                    hdimerscore = 8
                elif((homodimer.structure_found == True) and (homodimer.dg > -4500)):
                    hdimerscore = 7
                elif((homodimer.structure_found == True) and (homodimer.dg > -6000)):
                    hdimerscore = 6
                elif((homodimer.structure_found == True) and (homodimer.dg > -7500)):
                    hdimerscore = 5
                elif((homodimer.structure_found == True) and (homodimer.dg > -9000)):
                    hdimerscore = 4
                elif((homodimer.structure_found == True) and (homodimer.dg > -10500)):
                    hdimerscore = 3
                elif((homodimer.structure_found == True) and (homodimer.dg > -12000)):
                    hdimerscore = 2
                elif((homodimer.structure_found == True) and (homodimer.dg <= -13500)):
                    hdimerscore = 1

                if((gcpercent > 47) and (gcpercent < 53)):
                    gcscore = 5
                elif((gcpercent > 44) and (gcpercent < 56)):
                    gcscore = 4
                elif((gcpercent > 41) and (gcpercent < 59)):
                    gcscore = 3
                elif((gcpercent > 38) and (gcpercent < 62)):
                    gcscore = 2
                elif((gcpercent <= 38) or (gcpercent >= 62)):
                    gcscore = 1

                if(hairpin.structure_found == False):
                    hpinscore = 10
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 7))):
                    hpinscore = 9
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 6))):
                    hpinscore = 8
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 5))):
                    hpinscore = 7
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 4))):
                    hpinscore = 6
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 3))):
                    hpinscore = 5
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 2))):
                    hpinscore = 4
                elif((hairpin.structure_found == True) and (hairpin.tm < (annealingtemp - 1))):
                    hpinscore = 3
                elif((hairpin.structure_found == True) and (hairpin.tm < annealingtemp)):
                    hpinscore = 2
                elif((hairpin.structure_found == True) and (hairpin.tm >= annealingtemp)):
                    hpinscore = 1

                primer_score = lengthscore + mprimerscore + hdimerscore + gcscore + hpinscore
                primer_names.append(primer)
                primer_scores.append(primer_score)
    return primer_names, primer_scores


if __name__ == '__main__':

    primer_names, primer_scores = primerscore(sys.argv[1])

    for i in range(0, len(primer_names)):
        print("Primer: %s, score = %d" % (primer_names[i], primer_scores[i]))