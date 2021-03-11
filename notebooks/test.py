import pandas as pd
import os
from sqlalchemy import create_engine

def main():
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/molecular_prediction')

    query = '''
    SELECT
        magnetic_sheilding_tensors.*
        , structures.atom
        , structures.x
        , structures.y
        , structures.z	
        , mulliken_charges.mulliken_charge
        , scalar_coupling_contributions.atom_index_0
        , scalar_coupling_contributions.atom_index_1
        , scalar_coupling_contributions.type
        , scalar_coupling_contributions.fc
        , scalar_coupling_contributions.sd
        , scalar_coupling_contributions.pso
        , scalar_coupling_contributions.dso
        
    FROM
        magnetic_sheilding_tensors
    INNER JOIN
        mulliken_charges 
            ON 
                magnetic_sheilding_tensors.molecule_name = mulliken_charges.molecule_name
            AND
                magnetic_sheilding_tensors.atom_index = mulliken_charges.atom_index
    INNER JOIN
        structures
            ON
                magnetic_sheilding_tensors.molecule_name = structures.molecule_name
            AND
                magnetic_sheilding_tensors.atom_index = structures.atom_index
    INNER JOIN
        scalar_coupling_contributions
            ON
                magnetic_sheilding_tensors.molecule_name = scalar_coupling_contributions.molecule_name

    ORDER BY magnetic_sheilding_tensors.molecule_name ASC, magnetic_sheilding_tensors.atom_index  ASC

    '''
    # induvidual_atom_in_molecule = pd.read_sql(query,engine)
    # induvidual_atom_in_molecule
    return pd.read_sql(query,engine)

if __name__ == "__main__":
    print(main())