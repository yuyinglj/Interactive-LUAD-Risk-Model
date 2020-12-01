

"""
Args
    model_type: one of [LR, NN, DT, RF]
    genes: a list of genes to be used as features


     f(genes) = ___ 

     outputs
        - tumor or healthy cell
        - risk (live or die at some timeframe)


    sent to UI
        - prediction per patient
        - metrics
        - Ranked feature importance

"""

def create_model(model_type, genes):
    print("In create model.")
    print("\tType: ", model_type)
    print("\tGenes: ", genes)

    # TODO: write this method
   

    # TODO: what do we want to return to the UI?

    return {"metrics": {"ACC": .70, "F1": .57}, "model": model_type, "genes": genes}
    
