from .token_manager import TokenManager

class DataManager:
    @staticmethod
    def extract_car_specs(brand_code, model_code, model_year):
        token_manager = TokenManager()

        # Fetch vehicle specs using the TokenManager
        vehicle_specs = token_manager.get_vehicle_specs(brand_code, model_code, model_year)

        # # Select specific fields from vehicle_specs
        # selected_fields = []
        # car_type_mapping = {
        #     "เก๋ง": "110",
        #     "รถตู้": "210",
        #     "กระบะ": "320",
        # }

        # for spec in vehicle_specs:
        #     body_type = spec["BodyType"]
        #     voluntary_code = None

        #     # Check for keywords in BodyType to determine the voluntary code
        #     for keyword, code in car_type_mapping.items():
        #         if keyword in body_type:
        #             voluntary_code = code
        #             break  # Stop checking once a match is found

        #     selected_fields.append({
        #         "VehicleKey": spec["VehicleKey"],
        #         "ModelSpecDescEN": spec["ModelSpecDescEN"],
        #         "BodyType": body_type,
        #         "MinSumInsure": spec["MinSumInsure"],
        #         "MaxSumInsure": spec["MaxSumInsure"],
        #         "VoluntaryCode": voluntary_code  # Include the voluntary code
        #     })

        # return selected_fields
        return vehicle_specs
    
    def extract_package(self, package_type, voluntary_code, vehicle_key, province):
        token_manager = TokenManager()
        package = token_manager.get_package(package_type, voluntary_code, vehicle_key, province)
        print('get_package', package)
        # Prepare the transformed data
        transformed_packages = []
        
        # Mapping of GarageType values
        garage_type_mapping = {
            "ซ่อมอู่": "contracted",
            "ซ่อมห้าง": "dealer"
        }

        if package:
            for spec in package:           
                
                transformed_packages.append({
                    "package": {
                        "package_type": spec["PackageType"],
                        "name": spec["PackageName"],
                        "company": "Chubb",
                        "coverages": [
                            {
                                "coverage_type": coverage_type,
                                "name": coverage_name,
                                "value": coverage_value,
                            } for coverage_id, (coverage_type, coverage_name, coverage_value) in enumerate(
                                [
                                    ("1. Third party liability", "1.1 Bodily injury (Baht/Person)", spec["Coverage"]["AmountTPBIPerPerson"]),
                                    ("1. Third party liability", "Over maximum limit of compulsory motor insurance only (Baht/Accident)", spec["Coverage"]["AmountTPBIPerAccident"]),
                                    ("1. Third party liability", "1.2 Property damage (Baht/Accident)", spec["Coverage"]["AmountTPPDPerAccident"]),
                                    ("2. Own damage coverage", "2.1 Own damage", spec["Coverage"]["AmountODPerAccident"]),
                                    ("2. Own damage coverage", "2.2 Fire and theft", spec["Coverage"]["AmountFT"]),
                                    ("3. Additional coverage", "3.1 Personal accident (Baht/Person, Sedan:7/ Van:12/ Pickup:5)", spec["Coverage"]["AmountCoverMT01Driver13"]),
                                    ("3. Additional coverage", "3.2 Medical expenses (Baht/Person, Sedan:7/ Van:12/ Pickup:5)", spec["Coverage"]["AmountCoverMT02"]),
                                    ("3. Additional coverage", "3.3 Bail bond (Baht/Accident)", spec["Coverage"]["AmountCoverMT03"])
                                ],
                                start=1
                            )
                        ]
                    },
                    "min_sum_insured": spec["Coverage"].get("MinSumInsure", None),
                    "max_sum_insured": spec["Coverage"].get("MaxSumInsure", None),
                    "premium": spec["Premium"].get("PremiumTotal", None),
                    "deduct": spec.get("DeductTPPD", None),
                    "garage": garage_type_mapping.get(spec.get("GarageType"), spec.get("GarageType"))

                })
            
        return transformed_packages