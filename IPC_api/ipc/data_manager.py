from token_manager import TokenManager

class DataManager:
    @staticmethod
    def extract_car_specs(brand_code, model_code, model_year):
        token_manager = TokenManager()

        # Fetch vehicle specs using the TokenManager
        vehicle_specs = token_manager.get_vehicle_specs(brand_code, model_code, model_year)

        # Select specific fields from vehicle_specs
        selected_fields = []
        for spec in vehicle_specs:
            selected_fields.append({
                "VehicleKey": spec["VehicleKey"],
                "ModelSpecDescEN": spec["ModelSpecDescEN"],
                "MinSumInsure": spec["MinSumInsure"],
                "MaxSumInsure": spec["MaxSumInsure"],
            })
        return selected_fields
    
    def extract_package(self, package_type, voluntary_code, vehicle_key, province):
        token_manager = TokenManager()
        package = token_manager.get_package(package_type, voluntary_code, vehicle_key, province)

        # Prepare the transformed data
        transformed_packages = []
        
        # Mapping of GarageType values
        garage_type_mapping = {
            "ซ่อมอู่": "contracted",
            "ซ่อมห้าง": "dealer"
        }

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