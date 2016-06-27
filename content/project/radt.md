---
title: RAD-T
subtitle: predicting protein-protein interfaces
type: project
layout: single
img: img/project/rad-t.jpg
date: 2012-01-01
---

From 2011 to late 2013 I had the pleasure of working with Professor Murgita and many friends to make a protein-protein interface prediction pipeline.
My time with the project is done, but some of our work is described in a paper "Transient protein-protein interface prediction: datasets, features, algorithms, and the RAD-T predictor."
This paper is freely available to view here: http://www.ncbi.nlm.nih.gov/pubmed/24661439

The paper is highly academic (surprise!), and I hope to write a simpler description of the program and an introduction for anyone interested in protein research, but for now I include the paper's abstract below.

## Paper Abstract

### BACKGROUND

Transient protein-protein interactions (PPIs), which underly most biological processes, are a prime target for therapeutic development. Immense progress has been made towards computational prediction of PPIs using methods such as protein docking and sequence analysis. However, docking generally requires high resolution structures of both of the binding partners and sequence analysis requires that a significant number of recurrent patterns exist for the identification of a potential binding site. Researchers have turned to machine learning to overcome some of the other methods' restrictions by generalising interface sites with sets of descriptive features. Best practices for dataset generation, features, and learning algorithms have not yet been identified or agreed upon, and an analysis of the overall efficacy of machine learning based PPI predictors is due, in order to highlight potential areas for improvement.

### RESULTS

The presence of unknown interaction sites as a result of limited knowledge about protein interactions in the testing set dramatically reduces prediction accuracy. Greater accuracy in labelling the data by enforcing higher interface site rates per domain resulted in an average 44% improvement across multiple machine learning algorithms. A set of 10 biologically unrelated proteins that were consistently predicted on with high accuracy emerged through our analysis. We identify seven features with the most predictive power over multiple datasets and machine learning algorithms. Through our analysis, we created a new predictor, RAD-T, that outperforms existing non-structurally specializing machine learning protein interface predictors, with an average 59% increase in MCC score on a dataset with a high number of interactions.

### CONCLUSION

Current methods of evaluating machine-learning based PPI predictors tend to undervalue their performance, which may be artificially decreased by the presence of un-identified interaction sites. Changes to predictors' training sets will be integral to the future progress of interface prediction by machine learning methods. We reveal the need for a larger test set of well studied proteins or domain-specific scoring algorithms to compensate for poor interaction site identification on proteins in general.
