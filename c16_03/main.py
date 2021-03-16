
note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

##4 a/ calculez la moyenne de eleve1 

moyenne_eleve1 = (notes[0][2]+notes[1][2]+notes[2][2]+notes[3][2]+notes[4][2]+notes[5][2])/6
print(moyenne_eleve1)

##b/ calculez la moyenne de eleve1 en maths 
moyenne_eleve1_math = (notes[0][2]+notes[2][2]+notes[5][2])/3
print(moyenne_eleve1_math)

##c/ Créer une fonction "moyenne_tuples" qui calcule la moyenne de d'un élève dans une matière.


p=0
l= [1,2,3]

eleve = print(input("Eleve ?: "))
matiere  = print(input("Matiere ?: "))

def moyenne_tuples(notes,eleve=None,matiere=None) :  
    return sum(note[2] for note in notes, if (note[i][0] == eleve), if(note[i][1] == matiere):
                moyenne_tuples = notes_tuples[i][2]
                p += 1

    moyenne_tuples = moyenne/p
moyenne_tuples()

print(moyenne_tuples)

