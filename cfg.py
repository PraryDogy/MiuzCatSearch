import json
import os
import shutil

class Cfg:
    app_name = "MiuzCatSearch"

    app_ver: int = "1.0.5"
    images_dir: str = "/Volumes/Shares-1/Studio/Photo/Catalog"
    first_load: bool = True

    home_dir = os.path.expanduser("~")

    app_dir = os.path.join(
        home_dir,
        "Library",
        "Application Support",
        app_name,
        )

    catalog_json_file = os.path.join(
        app_dir,
        "catalog.json"
        )

    cfg_json_file = os.path.join(
        app_dir,
        "cfg.json"
        )
    
    @staticmethod
    def check_files():
        os.makedirs(Cfg.app_dir, exist_ok=True)

        if not os.path.exists(Cfg.catalog_json_file):
            shutil.copy2("catalog.json", Cfg.catalog_json_file)

        if not os.path.exists(Cfg.cfg_json_file):
            Cfg.write_cfg_json_file()

        data = Cfg.read_cfg_json_file()

        if type(data) != dict:
            Cfg.write_cfg_json_file()
            data = Cfg.read_cfg_json_file()

        if "app_ver" not in data or data["app_ver"] != Cfg.app_ver:
            Cfg.write_cfg_json_file()

        else:
            Cfg.first_load = data["first_load"]
            Cfg.images_dir = data["images_dir"]
            Cfg.write_cfg_json_file()


    @staticmethod
    def read_cfg_json_file() -> dict:
        try:
            with open(Cfg.cfg_json_file, "r", encoding="utf=8") as file:
                return json.load(file)
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def write_cfg_json_file():
        new_data = {
            "app_ver": Cfg.app_ver,
            "images_dir": Cfg.images_dir,
            "first_load": Cfg.first_load
            }

        with open(Cfg.cfg_json_file, "w", encoding="utf=8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def read_catalog_json_file() -> dict:
        with open(Cfg.catalog_json_file, "r", encoding='utf-8') as json_file:
            return json.loads(json_file.read())
        
    @staticmethod
    def write_catalog_json_file(new_data: dict):
        with open(Cfg.catalog_json_file, "w", encoding="utf=8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=2)

    @staticmethod
    def get_default_settings():
        return {
            "app_ver": Cfg.app_ver,
            "images_dir": Cfg.images_dir,
            "first_load": True
            }