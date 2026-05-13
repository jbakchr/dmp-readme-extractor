Title of the dataset:
Supporting data for Non-extractable residues (NER) in persistence assessment - effect on the degradation half-life of chemicals


Version of dataset:
1


Creators (include contact and ORCID):
Cindy Michala Jespersen, contact: cindymjespersen@gmail.com, ORCID: 0009-0006-8045-8936


Contributors:
Stefan Trapp, ORCID: 0000-0001-8968-6296
Matthias Kästner, ORCID: 0000-0003-4041-6257


Related publication:
Non-extractable residues (NER) in persistence assessment - effect on the degradation half-life of chemicals


This dataset contains the following files:
Data from degradation studies.xlsx
MTB sheet.xlsx
Scenarios for input to CAKE.xlsx
Reactions.docx
SFO outputs from CAKE.docx
DFOP outputs from CAKE.docx
Folder: CAKE-files, contains the following files (all in .csf format meaning CAKE Study File): 
2,4-D.csf
Acetaminophen.csf
Atrazine.csf
Benzovindiflupyr.csf
Bromoxynil.csf
C-DA+.csf
C-DP.csf
C-DS.csf
Celecoxib.csf
Ciprofloxacin.csf
Deltamethrin.csf
Dicamba.csf
Fenoxycarb.csf
Glyphosate.csf
Ibuprofen.csf
Isoproturon.csf
Lindane.csf
Metamitron.csf
Pyriproxyfen.csf 
Sulfadiazine.csf
Thiamethoxam.csf
Triclosan.csf
Trifluralin.csf
Voriconazole.csf


Description:
Data has been collected from already published studies on chemical degradation in OECD 307, 308 or 309 tests or similar tests. All collected data is presented in the Excel-file "Data from degradation studies". In some studies the data was only presented in graphs. Here, the tool PlotDigitizer was used to extract the data from the graphs.
Included studies has extractable parent substance, CO2, and NER measured at at least 5 timepoints.
For all substances we had data for, a reaction equation was set up using a set of rules determined for use for the Microbial Turnover to Biomass (MTB) method. The reaction assumed for each substance can be found in the Word-file "Reactions".
With the reaction, we could move on to predict the amount of bioNER developed during each study, using the MTB method. The calculations for each substance is seen in the Excel file "MTB sheet"
Combining the data from the studies and the results from the MTB calculations, we investigated how different approached towards NER affected the degradation curve. The 4 investigated scenarios are set up for each substance in the Excel-file "Scenarios for input to CAKE".

For the following substances, a relevant metabolite has been modelled as well: glyphosate, thiamethoxam, triclosan.
The unit is %aL (% applied label) which is the percentage of the initially added compound. The tested compound is labelled, in order to follow its fate throughout the study.
3 scenarios were assessed for each laboratory test where the included amount of NER vary: 
i) Parent only: only measured extractable parent compound (except for the starting value at time 0, where any formed metabolite or NER is added to the extractable parent too). 
ii) Parent + tNER: extracted parent compound + total amount of NER measured.
iii) Parent + (tNER - MTBbioNER): Same as ii) Parent + tNER, except that the amount of bioNER calculated with the MTB method has been subtracted.
In cases where measurements of NER I has been performed, an extra scenario is included, as NER I is considered to be the potentially hazardous part of NER:
iv) Parent + NER I: Measured amount of extractable parent compound + measured amount of NER I, determined with either silylation or EDTA extraction.

We investigated the degradation kinetics for 24 substances in the program CAKE (Computer Assisted Kinetic Evaluation). CAKE is available for download at https://cake-kinetics.org/, all CAKE-files from the study are in the folder CAKE-files.
Each substance has its own CAKE file, which contains data from one or more laboratory studies on that substance.

Where more studies have been performed with the same substance, all tests are included in the CAKE file, distinguished by eg. an abbreviation of their difference (eg. if two tests were made, and the OECD tests differ between the two (so OECD 308 and 309 has been made), one dataset will have 308 on all sheet names related to the OECD 308 test and the sheets related to the OECD 309 test, will have 309 in the name.

As a backup of our results, we copied the outputs from CAKE to Word-files, in case someone without access to CAKE would like to investigate our results. We divided the outputs into two different files, depending on the chosen degradation kinetic, either SFO (used in the article) or DFOP.
These are found in the Word-files "SFO outputs from CAKE" and "DFOP outputs from CAKE" 


Keywords:
Bound residues
DT50
DegT50
Microbial Turnover to Biomass
Pesticides
bioNER
XenoNER
PBT
Risk Assessment
REACH


Explanation of variables:
Time: Measured in days. Given in the studies we collected data from
Parent or extractable parent: The amount of extractable parent compound/investigated compound measured in the studies in %aL (% applied label)
CO2: Amount of CO2 measured in %aL 
NER: Measured total amount of non-extractable residues in %aL. In the scenarios this is the same as tNER (short for total NER).
MTBbioNER: The amount of bioNER predicted with the MTB method. Given in %aL.
The variables related to the MTB method has been described in other articles related to the MTB method, and will therefore not be repeated here.
NER I: Amount of NER physically entrapped or sorbed. This is measured in some of the studies by either silylation or EDTA extraction. Unit is %aL.
Metabolite: Relevant for compounds forming >10 %aL of a specific metabolite at any time during the experiment. Unit is %aL. 
Fraction to this pathway (in the Excel-file: Scenarios for input to CAKE.xlsx): When a metabolite is relevant, a specific reaction equation has been made for a pathway forming the metabolite. It is assumed that the %aL taking this pathway is the highest measured amount of metabolite at any timepoint. The rest of the %aL goes through the other/standard pathway. 


Methods, materials and software:
The method Microbial Turnover to Biomass (MTB) was used, other methods see project description. 
For .csf-files, relevant software: CAKE (Computer Assisted Kinetic Evaluation) - degradation kinetics program, available for download at https://cake-kinetics.org/.
For .xslx-files: Microsoft Excel or other open-source alternatives


Funding:
Bekæmpelsesmiddelforskningsprogrammet at Miljøstyrelsen (The Pesticide Research Programme at the Danish EPA)


How to cite this data:
Jespersen CM, Trapp S, Kästner M (2024) Supporting data for Non-extractable residues (NER) in persistence assessment - effect on the degradation half-life of chemicals (DOI: https://doi.org/10.11583/DTU.27646149)
This dataset is published under the CC BY 4.0 license.
This license allows reusers to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator.
