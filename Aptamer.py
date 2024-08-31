from aptatrans_pipeline import AptaTransPipeline

pipeline = AptaTransPipeline(
    dim=128,
    mult_ff=2,
    n_layers=6,
    n_heads=8,
    dropout=0.1,
    load_best_pt=False,
    device='cuda',
    seed=1004,
)


pipeline.set_data_rna_pt(batch_size=32) # dataset from bpRNA
pipeline.pretrain_encoder_aptamer(epochs=10, lr=1e-5)

pipeline.set_data_protein_pt(batch_size=32) # dataset from PDB
pipeline.pretrain_encoder_protein(epochs=1000, lr=1e-5)

pipeline.set_data_for_training(batch_size=16)
pipeline.train(epochs=200, lr=1e-5)


print('********************************************************************************************************************************************************')
print('Prueba')
# your aptamer
aptamer1 = 'AACGCCGCGCGUUUAACUUCC'

# target protein
target1 = 'STEYKLVVVGADGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQGVDDAFYTLVREIRKHKEKMSK'

pipeline.inference(aptamer1, target1)

print('********************************************************************************************************************************************************')



print('********************************************************************************************************************************************************')
print('Noggin 7AG0 sugerencia=5')

# Target protein sequence
target2 = 'MQHYLHIRPAPSDNLPLVDLIEHPDPIFDPKEKDLNETLLRSLLGGHYDPGFMATSPPEDRPGGGGGAAGGAEDLAELDQLLRQRPSGAMPSEIKGLEFSEGLAQGKKQRLSKKLRRKLQMWLWSQTFCPVLYAWNDLGSRFWPRYVKVGSCFSKRSCSVPEGMVCKPSKSVHLTVLRWRCQRRGGQRCGWIPIQYPIISECKCSC'
# Recommend with AptaTransPipeline (consists of Apta-MCTS and AptaTrans)
pipeline.recommend(target2, n_aptamers=5, depth=40, iteration=1000)

print('********************************************************************************************************************************************************')



print('********************************************************************************************************************************************************')
print('Noggin 7AG0 sugerencia= 15')

# Target protein sequence
target3 = 'STEYKLVVVGADGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQGVDDAFYTLVREIRKHKEKMSK'
# Recommend with AptaTransPipeline (consists of Apta-MCTS and AptaTrans)
pipeline.recommend(target3, n_aptamers=5, depth=40, iteration=1000)

print('********************************************************************************************************************************************************')



print('********************************************************************************************************************************************************')
print('BMP-2 P12643')

# Target protein sequence
target4 = 'MVAGTRCLLALLLPQVLLGGAAGLVPELGRRKFAAASSGRPSSQPSDEVLSEFELRLLSMFGLKQRPTPSRDAVVPPYMLDLYRRHSGQPGSPAPDHRLERAASRANTVRSFHHEESLEELPETSGKTTRRFFFNLSSIPTEEFITSAELQVFREQMQDALGNNSSFHHRINIYEIIKPATANSKFPVTRLLDTRLVNQNASRWESFDVTPAVMRWTAQGHANHGFVVEVAHLEEKQGVSKRHVRISRSLHQDEHSWSQIRPLLVTFGHDGKGHPLHKREKRQAKHKQRKRLKSSCKRHPLYVDFSDVGWNDWIVAPPGYHAFYCHGECPFPLADHLNSTNHAIVQTLVNSVNSKIPKACCVPTELSAISMLYLDENEKVVLKNYQDMVVEGCGCR'
# Recommend with AptaTransPipeline (consists of Apta-MCTS and AptaTrans)
pipeline.recommend(target4, n_aptamers=5, depth=40, iteration=1000)

print('********************************************************************************************************************************************************')



print('********************************************************************************************************************************************************')
print('BMP-4 P12644')

# Target protein sequence
target5 = 'MIPGNRMLMVVLLCQVLLGGASHASLIPETGKKKVAEIQGHAGGRRSGQSHELLRDFEATLLQMFGLRRRPQPSKSAVIPDYMRDLYRLQSGEEEEEQIHSTGLEYPERPASRANTVRSFHHEEHLENIPGTSENSAFRFLFNLSSIPENEVISSAELRLFREQVDQGPDWERGFHRINIYEVMKPPAEVVPGHLITRLLDTRLVHHNVTRWETFDVSPAVLRWTREKQPNYGLAIEVTHLHQTRTHQGQHVRISRSLPQGSGNWAQLRPLLVTFGHDGRGHALTRRRRAKRSPKHHSQRARKKNKNCRRHSLYVDFSDVGWNDWIVAPPGYQAFYCHGDCPFPLADHLNSTNHAIVQTLVNSVNSSIPKACCVPTELSAISMLYLDEYDKVVLKNYQEMVVEGCGCR'
# Recommend with AptaTransPipeline (consists of Apta-MCTS and AptaTrans)
pipeline.recommend(target5, n_aptamers=5, depth=40, iteration=1000)

print('********************************************************************************************************************************************************')



print('********************************************************************************************************************************************************')
print('BMPR-1A P36894')

# Target protein sequence
target6 = 'MPQLYIYIRLLGAYLFIISRVQGQNLDSMLHGTGMKSDSDQKKSENGVTLAPEDTLPFLKCYCSGHCPDDAINNTCITNGHCFAIIEEDDQGETTLASGCMKYEGSDFQCKDSPKAQLRRTIECCRTNLCNQYLQPTLPPVVIGPFFDGSIRWLVLLISMAVCIIAMIIFSSCFCYKHYCKSISSRRRYNRDLEQDEAFIPVGESLKDLIDQSQSSGSGSGLPLLVQRTIAKQIQMVRQVGKGRYGEVWMGKWRGEKVAVKVFFTTEEASWFRETEIYQTVLMRHENILGFIAADIKGTGSWTQLYLITDYHENGSLYDFLKCATLDTRALLKLAYSAACGLCHLHTEIYGTQGKPAIAHRDLKSKNILIKKNGSCCIADLGLAVKFNSDTNEVDVPLNTRVGTKRYMAPEVLDESLNKNHFQPYIMADIYSFGLIIWEMARRCITGGIVEEYQLPYYNMVPSDPSYEDMREVVCVKRLRPIVSNRWNSDECLRAVLKLMSECWAHNPASRLTALRIKKTLAKMVESQDVKI'
# Recommend with AptaTransPipeline (consists of Apta-MCTS and AptaTrans)
pipeline.recommend(target6, n_aptamers=5, depth=40, iteration=1000)

print('********************************************************************************************************************************************************')