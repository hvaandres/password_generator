import itertools

# Linux and Windows hashes
linux_hashes = [
    "elphaba:$1$N0QRDJP/$pbLARXUh7eHHaUfRVsDZB1:16709:0:99999:7:::",
    "glinda:$1$r49XI/MC$Qv9Tzn3Na4lpXcATgsXUb0:16709:0:99999:7:::",
    "fiyero:$1$wwJBf/a9$VZ.AjP18HzZOrk6EgpSCE1:16709:0:99999:7:::",
    "morrible:$1$.cTIU/P2$IzCxFSA6O6LbgIb4ZqxXL0:16709:0:99999:7:::",
    "wizard:$1$mGcg1RQS$hVgeg5qt5n1vLCV3u525z.:16709:0:99999:7:::",
    "nessarose:$1$sVdIhKTa$I3TkrsPNJvVqFfsmp4t4s0:16709:0:99999:7:::",
    "boq:$1$/mYxkJtu$Fov4cggA9GOkjkC.fgxUO1:16709:0:99999:7:::",
    "dillamond:$1$brz8O/3l$/sCMgksaCmbSRcQ.wszuo0:16709:0:99999:7:::",
    "dorothy:$1$KIOe8VoR$yU/ZtAIkKpBwEIwZI9Ji00:16709:0:99999:7:::",
    "toto:$1$qmoIw/nQ$yfBc6TXkWsa7yTdP/Fy.A/:16709:0:99999:7:::",
    "lion:$1$ZJEFY/MR$aNelGtObgl3IUgas0UOz0.:16709:0:99999:7:::",
    "scarecrow:$1$15uSqOfj$UzbhoXkHSgRi/0IV51kbu1:16709:0:99999:7:::",
    "tinman:$1$GrRnrrn2$ErDA67kNCSFOF38gzEGzf/:16709:0:99999:7:::",
    "munchkin:$1$bQRLq9NN$PCkVgsF2yQuRXE0j4BXA.1:16709:0:99999:7:::",
    "easy:$1$Lxxc4/cs$zCU.CHV3a9jL/yONrpfy21:16709:0:99999:7:::",
    "lesseasy:$1$NxueFlzN$Q7KM3mqp7.L76Hsgb2lLH0:16709:0:99999:7:::",
    "lesseasy2:$1$yHSqL/F2$u1sujIeZZK48pN1kbIxIr0:16709:0:99999:7:::",
    "lesseasyist:$1$7CWomuEo$KuIK0Sv70TWfj1sOtkqUp0:16709:0:99999:7:::"
]

windows_hashes = [
    "ariel:1015:NO PASSWORD*********************:B659BA8F0504F88B3D89AAACF20F14F1:::",
    "callisto:1011:NO PASSWORD*********************:0742CCD45B3C7F97E6A24998CA6BDE0A:::",
    "europa:1008:54443EBF236958C85E57FC0295493699:9501B3D00BA48C8382CEBCDBAA73A8A1:::",
    "ganymede:1010:877147F7D7CD2C3CAAD3B435B51404EE:FF8F38C0AAFE3FF68F4B5F97EF44FC5F:::",
    "io:1007:8C873B92FABE5205417EAF50CFAC29C3:797A9DE4B8AB33DE99757B61518C256F:::",
    "leda:1009:5D567324BA3CCEF8D9243782006C7417:531175CF1EA902821AE1222C1ACD2649:::",
    "metis:1012:NO PASSWORD*********************:4015F807F0471F24F2808B82F25F4984:::",
    "mimas:1006:3562C4932A05E4DF5567991398D2E00E:81C38183020AE4A0BAFB0008363D7B96:::",
    "oberon:1016:NO PASSWORD*********************:9C51795067EAD4DF2F53A142B19E3FC3:::",
    "rhea:1004:1D0FF108FB745360AAD3B435B51404EE:CFCD184EF8E19E90E21FAE5B5E10D1C9:::",
    "thebe:1013:NO PASSWORD*********************:A7964C61D6DBBB0341E7105A5F1B70E4:::",
    "titan:1005:14A256F4F58DAD24AAD3B435B51404EE:FA47505133A402F28C361FB31D305CE8:::",
    "titania:1018:NO PASSWORD*********************:6EB52D4E8C2939B26447A6539E3C453A:::",
    "tooeasy:1019:NO PASSWORD*********************:4803D59B0E934D69D2048EC9582DBFC1:::",
    "triton:1014:NO PASSWORD*********************:214E90B41E2752D80ACD34E13F3E9831:::",
    "umbriel:1017:NO PASSWORD*********************:B4AC84891202F6AD8386AA65E854B6FF:::",
    "way2easy:1020:NO PASSWORD*********************:BECEDB42EC3C5C7F965255338BE4453C:::"
]

# Extract usernames from the hashes
usernames = [hash.split(':')[0] for hash in linux_hashes + windows_hashes]

# Generate simple variations based on usernames
def generate_password_variations(usernames):
    variations = []
    for username in usernames:
        variations.extend([
            username,
            f"{username}123",
            f"{username}@123",
            f"{username}2024",
            f"{username}!@#",
            f"{username}password"
        ])
    return variations

# Get the password variations
password_variations = generate_password_variations(usernames)

# Trim to 50 passwords
final_password_list = password_variations[:200]

# Save to rockyou.txt
with open('rockyou.txt', 'w') as file:
    for password in final_password_list:
        file.write(password + '\n')

# Verify the number of lines in rockyou.txt
print(f"Number of passwords in rockyou.txt: {len(final_password_list)}")
