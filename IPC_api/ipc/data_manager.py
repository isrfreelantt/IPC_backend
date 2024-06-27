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

# Usage
data_manager = DataManager()