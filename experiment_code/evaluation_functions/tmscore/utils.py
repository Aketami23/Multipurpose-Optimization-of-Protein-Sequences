import subprocess
import re
from config_utils import load_config

def calculate_tmscore(purpose_pdb: str, new_pdb: str, config_path: str) -> float:
    _config = load_config(config_path)
    usalign_path = _config["usalign_path"]
    tm_command = [
        usalign_path,
        purpose_pdb,
        new_pdb,
        "-TMscore",
        "1"
    ]

    # 実行内容を明示的に表示
    print("Running command:", " ".join(tm_command))

    # サブプロセス実行
    tm_result = subprocess.run(tm_command, shell=False, capture_output=True, text=True)

    # 結果をすべて出力（標準出力と標準エラー）
    print("STDOUT:\n", tm_result.stdout)
    print("STDERR:\n", tm_result.stderr)

    # 正規表現でTM-scoreを検索
    tm_match = re.search(r"TM-score=\s*([0-9.]+)", tm_result.stdout)

    if tm_match:
        tm_score = float(tm_match.group(1))
        return -tm_score  # Return negative value for minimization
    else:
        print("ERROR: TM-score not found in output.")
        return 0.0



def calculate_default_tmscore(purpose_pdb: str, new_pdb: str, config_path: str) -> float:
    _config = load_config(config_path)
    usalign_path = _config["usalign_path"]
    tm_command = [
        usalign_path,
        purpose_pdb,
        new_pdb,
        "-TMscore",
        "0"
    ]
    tm_result = subprocess.run(tm_command, shell=False, capture_output=True, text=True)
    tm_match = re.search(r"TM-score=\s*([0-9.]+)", tm_result.stdout)
    tm_score = float(tm_match.group(1))
    return - tm_score # Return negative value for minimization