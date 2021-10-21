# Database mongodb --> dbpenguin

## 1 Collection 
### penguin_details {
            "specie": specie,
            "weight": weight,
            "sex": sex, 
            "location": {"region": region, "island": island}
            "culmen_length_mm": culmen_length_mm, 
            "culmen_depth_mm": culmen depth (mm),
            "lipper_length_mm": lipper_length_mm, 
            "body_mass_g" : body_mass_g
        }

## 2. Collection
### distribution_details {

    "species" : ["chinstrap", "adelie", "gentoo"], 
    "average_weight": {"chinstrap": promedio, "adelie": promedio, "gentoo":promedio},
    "penguins_by_island" : {"dream": count_penguin, "torgersen": count_penguin, "biscoe": count_penguin},
    "total_penguins_by_sex" : { "total_sex_type" : {"male": cantidad, "famele": cantidad }, 
                                "sex_type_by_island" : {
                                    "dream" : {"male": cantidad, "famele": cantidad }, 
                                    "torgersen" : {"male": cantidad, "famele": cantidad }, 
                                    "biscoe" : {"male": cantidad, "famele": cantidad } 
                                }
                        },
    "species_distribution" : {"chinstrap": {"dream": count_penguin, "torgersen": count_penguin, "biscoe": count_penguin},
                              "adelie": {"dream": count_penguin, "torgersen": count_penguin, "biscoe": count_penguin},
                              "gentoo": {"dream": count_penguin, "torgersen": count_penguin, "biscoe": count_penguin}
                            }

}

## 3. Collection 
#### penguin_breeding_signy {
    
    "location" {"region: "Southern Atlantic", "island": Signy Island}: 
    "year" : year, 
    #number of pairs that can reproduce
    "breeding_pairs" : {"chinstrap": count_pairs, 
                        "adelie": count_pairs,
                        "gentoo": count_pairs
                        },
    ##number chicks fledged per pair                
    "chicks_fledged_per_pair" : {"chinstrap": count_pairs,
                                "adelie": count_pairs,
                                "gentoo": count_pairs
                        }

    "average_born_by_species" : {"chinstrap": pairs * chicks by pair,
                                "adelie": pairs * chicks by pair,
                                "gentoo": pairs * chicks by pair,
                        }
}

                
                
                
        