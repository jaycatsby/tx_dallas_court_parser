#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module offers regular expressions for each information table.
"""
from __future__ import unicode_literals
import re

##########################################################################
#####                        ROWS TO IGNORE                          #####
##########################################################################
FILTER_REGEX = re.compile(r'^(¢|A010|B050|B060|B070|C010|C015|Mon|Tue|Wed|Thu|Fri|Sat|Sun)')

##########################################################################
#####                            HEADER                              #####
##########################################################################
DA_CASE_ID_REGEX = re.compile(r'(?<=DA CASE ID )(.+)(?= JUDCL CASE ID)')
JD_CASE_ID_REGEX = re.compile(r'(?<=JUDCL CASE ID )(.+)$')

##########################################################################
#####                      JUDICIAL INFORMATION                      #####
##########################################################################
### JUDICIAL_TRS[0]
DEF_NAME_REGEX = re.compile(r'(?<=DEF NAME )(.+)(?= RACE)')
DEF_RACE_REGEX = re.compile(r'(?<=RACE )(.+)(?= SEX)')
DEF_SEX_REGEX = re.compile(r'(?<=SEX )(.+)(?= DOB)')
DEF_DOB_REGEX = re.compile(r'(?<=DOB )(.+)(?=AGE)')
DEF_AGE_REGEX = re.compile(r'(?<=AGE )(.+)$')
### JUDICIAL_TRS[1]
DEF_ADDR_REGEX = re.compile(r'(?<=DEF ADR1)(.+)(?= AC)')
DEF_AC_REGEX = re.compile(r'(?<=AC )(.+)(?= PH)')
DEF_PH_REGEX = re.compile(r'(?<=PH )(.+)(?= SS)')
DEF_SS_REGEX = re.compile(r'(?<=SS )(.+)$')
### JUDICIAL_TRS[2]
DEF_CITY_REGEX = re.compile(r'(?<=DEF CITY )(.+)(?= ST )')
DEF_STATE_REGEX = re.compile(r'(?<=ST )(.+)(?= ZIP)')
DEF_ZIP_REGEX = re.compile(r'(?<=ZIP )(.+)(?= DLNUM)')
DEF_DL_NUM_REGEX = re.compile(r'(?<=DLNUM )(.+)(?= DLST)')
DEF_DL_STATE_REGEX = re.compile(r'(?<=DLST )(.+)$')
### JUDICIAL_TRS[3]
DEF_OFF_REGEX = re.compile(r'(?<=OFF )(.+)(?= DT)')
DEF_OFF_DT_REGEX = re.compile(r'(?<=DT )(.+)(?= TYP/CL)')
DEF_OFF_TYP_CLS_REGEX = re.compile(r'(?<=TYP/CL )(.+)(?= GOC/CAT)')
DEF_OFF_GOC_CAT_REGEX = re.compile(r'(?<=GOC/CAT )(.+)(?= CODE)')
DEF_OFF_CODE_REGEX = re.compile(r'(?<=CODE )(.+)$')
### JUDICIAL_TRS[4]
DEF_COMT_REGEX = re.compile(r'(?<=COMT )(.+)(?= SID NUM)')
DEF_SID_NUM_REGEX = re.compile(r'(?<=SID NUM )(.+)(?= (OF AMT|NAMELY))')
DEF_OF_AMT_REGEX = re.compile(r'(?<=OF AMT )(.+)$')
### JUDICIAL_TRS[5]
DEF_COMPLAINANT_REGEX = re.compile(r'(?<=COMPLAINANT )(.+)(?= TAPE #)')
DEF_TAPE_NUM_REGEX = re.compile(r'(?<=TAPE # )(.+)(?= ARREST DATE)')
DEF_ARREST_DATE_REGEX = re.compile(r'(?<=ARREST DATE )(.+)$')
### JUDICIAL_TRS[6]
DEF_JUV_STAT_REGEX = re.compile(r'(?<=JUV STAT )(.+)(?= REPEAT OFFENDER)')
DEF_REPEAT_STAT_REGEX = re.compile(r'(?<=REPEAT OFFENDER )(.+)(?= CAREER OFFENDER)')
DEF_CAREER_STAT_REGEX = re.compile(r'(?<=CAREER OFFENDER )(.+)(?= ORIG-LOC)')
DEF_ORIG_LOC_REGEX = re.compile(r'(?<=ORIG-LOC )(.+)(?= CURR-LOC)')
DEF_CURR_LOC_REGEX = re.compile(r'(?<=CURR-LOC )(.+)$')
### JUDICIAL_TRS[7]
DEF_FILING_AGENCY_REGEX = re.compile(r'(?<=FILING AGENCY)(.+)(?= SER/CAS NO)')
DEF_SER_CASE_NUM_REGEX = re.compile(r'(?<=SER/CAS NO)(.+)(?= ARREST NUM)')
DEF_ARREST_NUM_REGEX = re.compile(r'(?<=ARREST NUM )(.+)$')
### JUDICIAL_TRS[8]
DEF_LAI_NUM_REGEX = re.compile(r'(?<=LAI NUM)(.+)(?= AIS/DSO NO)')
DEF_AIS_DSO_NUM_REGEX = re.compile(r'(?<=AIS/DSO NO)(.+)(?= BOOKIN NUM)')
DEF_BOOKING_NUM_REGEX = re.compile(r'(?<=BOOKIN NUM )(.+)$')
### JUDICIAL_TRS[9]
DEF_JP_FILE_DATE_REGEX = re.compile(r'(?<=JP FILE DATE )(.+)(?= JP CASE ID)')
DEF_JP_CASE_ID_REGEX = re.compile(r'(?<=JP CASE ID )(.+)(?= JP COURT ID)')
DEF_JP_COURT_ID_REGEX = re.compile(r'(?<=JP COURT ID )(.+)(?= FED )')
DEF_FED_REGEX = re.compile(r'(?<=FED )(.+)(?= EVH )')
DEF_EVH_REGEX = re.compile(r'(?<=EVH )(.+)(?= AFF )')
DEF_AFF_REGEX = re.compile(r'(?<=AFF )(.+)$')
### JUDICIAL_TRS[10]
DEF_MAGIS_DATE_REGEX = re.compile(r'(?<=MAGISTRATE DATE )(.+)(?= MAGIS COURT)')
DEF_MAGIS_COURT_REGEX = re.compile(r'(?<=MAGIS COURT )(.+)(?= MAGIS JUDGE)')
DEF_MAGIS_JUDGE_REGEX = re.compile(r'(?<=MAGIS JUDGE )(.+)(?= BOUND OVER)')
DEF_BOUND_OVER_REGEX = re.compile(r'(?<=BOUND OVER )(.+)$')
### JUDICIAL_TRS[11]
DEF_EXAM_TRIAL_DATE_REGEX = re.compile(r'(?<=EXAM TRIAL DATE )(.+)(?= EXAM  COURT)')
DEF_EXAM_COURT_REGEX = re.compile(r'(?<=EXAM  COURT )(.+)(?= EXAM  JUDGE)')
DEF_EXAM_JUDGE_REGEX = re.compile(r'(?<=EXAM  JUDGE )(.+)(?= IND METH)')
DEF_IND_METHOD_REGEX = re.compile(r'(?<=IND METH )(.+)$')
### JUDICIAL_TRS[12]
DEF_GJ_H_R_DATE_REGEX = re.compile(r'(?<=GJ/H/R DT )(.+)(?= GJ# )')
DEF_GJ_NUM_REGEX = re.compile(r'(?<=GJ# )(.+)(?= GJ/W/FILE )')
DEF_GJ_W_FILE_DATE_REGEX = re.compile(r'(?<=GJ/W/FILE )(.+)(?= GJ DS)')
DEF_GJ_DS_REGEX = re.compile(r'(?<=GJ DS )(.+)(?= DA DSP)')
DEF_DA_DSP_REGEX = re.compile(r'(?<=DA DSP )(.+)(?= ACC)')
DEF_ACC_REGEX = re.compile(r'(?<=ACC )(.+)(?= REAS )')
DEF_REAS_REGEX = re.compile(r'(?<=REAS )(.+)$')
### JUDICIAL_TRS[13]
DEF_DA_DISP_DATE_REGEX = re.compile(r'(?<=DA DISPOS  DATE )(.+)(?= MISDEMEANOR REDUCTION)')
DEF_MISD_REDUC_REGEX = re.compile(r'(?<=MISDEMEANOR REDUCTION )(.+)(?= SENTENCE PROBATED)')
DEF_SENT_PROB_REGEX = re.compile(r'(?<=SENTENCE PROBATED )(.+)$')
### JUDICIAL_TRS[14]
DEF_JUDCL_CASE_ID_REGEX = re.compile(r'(?<=JUDCL CASE ID )(.+)(?= GJ CT )')
DEF_GJ_CT_REGEX = re.compile(r'(?<=GJ CT )(.+)(?= PROS STAT )')
DEF_PROS_STAT_REGEX = re.compile(r'(?<=PROS STAT )(.+)(?= PROS NAME)')
DEF_PROS_NAME_REGEX = re.compile(r'(?<=PROS NAME )(.+)$')
### JUDICIAL_TRS[15]
DEF_COURT_ASSIGNED_TO_REGEX = re.compile(r'(?<=COURT ASSIGNED TO )(.+)(?= DATE ASSIGNED )')
DEF_DATE_ASSIGNED_REGEX = re.compile(r'(?<=DATE ASSIGNED )(.+)(?= ASSIGNED BY )')
DEF_ASSIGNED_BY_REGEX = re.compile(r'(?<=ASSIGNED BY )(.+)(?= REASON )')
DEF_REASON_REGEX = re.compile(r'(?<=REASON )(.+)$')
### JUDICIAL_TRS[16]
DEF_PRE_CASE_ID_REGEX = re.compile(r'(?<=PRECEEDING DA CASE ID )(.+)(?= SUCCEEDING DA CASE ID)')
DEF_SUC_CASE_ID_REGEX = re.compile(r'(?<=SUCCEEDING DA CASE ID )(.+)$')
### JUDICIAL_TRS[17]
DEF_TRN_REGEX = re.compile(r'(?<=TRN )(.+)(?= TRS)')
DEF_TRS_REGEX = re.compile(r'(?<=TRS )(.+)(?= WARRANT STATUS )')
DEF_WARR_STAT_REGEX = re.compile(r'(?<=WARRANT STATUS )(.+)(?= STATE OFF CD)')
DEF_STATE_OFF_CD_REGEX = re.compile(r'(?<=STATE OFF CD )(.+)$')

##########################################################################
#####                         SETS AND PASSES                        #####
##########################################################################
### Line 1
SET_DATE_REGEX = re.compile(r'(?<=SET FOR DATE )(.+)(?= SET FOR TIME)')
SET_TIME_REGEX = re.compile(r'(?<=SET FOR TIME )(.+)(?= SET TYPE)')
SET_TYPE_REGEX = re.compile(r'(?<=SET TYPE )(.+)(?= PASSED TO DATE)')
SET_PASSED_DATE_REGEX = re.compile(r'(?<=PASSED TO DATE )(.+)$')
### Line 2
SET_DISP_CODE_REGEX = re.compile(r'(?<=SET DISPOSITION CODE )(.+)(?= PASSED GENERALLY )')
SET_PASS_GEN_REGEX = re.compile(r'(?<=PASSED GENERALLY )(.+)(?= COMMENTS)')
SET_COMMENTS_REGEX = re.compile(r'(?<=COMMENTS )(.+)$')
### Line 3
SET_STATES_REC_REGEX = re.compile(r'(?<=STATES RECOMMENDATION )(.+)(?= REC NO)')
SET_REC_NUM_REGEX = re.compile(r'(?<=REC NO )(.+)$')

##########################################################################
#####                              NAMES                             #####
##########################################################################
### Line 1
NAME_ASSOC_REGEX = re.compile(r'(?<=ASSOCIATED NAME )(.+)(?= NAME REF CODE)')
NAME_REF_CODE_REGEX = re.compile(r'(?<=NAME REF CODE )(.+)$')
### Line 2
NAME_CT_APPT_REGEX = re.compile(r'(?<=CT APPOINTED )(.+)(?= BAR NO )')
NAME_BAR_NO_REGEX = re.compile(r'(?<=BAR NO )(.+)(?= BOND MAKER)')
NAME_BOND_MAKER_REGEX = re.compile(r'(?<=BOND MAKER )(.+)(?= DT BOND MADE)')
NAME_BOND_MADE_REGEX = re.compile(r'(?<=DT BOND MADE )(.+)$')

##########################################################################
#####                             CHARGE                             #####
##########################################################################
### Line 1
CHRG_NAME_REGEX = re.compile(r'(?<=DEF NAME )(.+)(?= OFFENSE CD)')
CHRG_OFF_CD_REGEX = re.compile(r'(?<=OFFENSE CD )(.+)(?= STATE CD)')
CHRG_STATE_CD_REGEX = re.compile(r'(?<=STATE CD )(.+)$')
### Line 2
CHRG_DESC_REGEX = re.compile(r'(?<=DESC )(.+)(?= COMT)')
CHRG_COMT_REGEX = re.compile(r'(?<=COMT )(.+)(?= TYP/CL)')
CHRG_TYPE_CL_REGEX = re.compile(r'(?<=TYP/CL )(.+)(?= GOC)')
CHRG_GOC_REGEX = re.compile(r'(?<=GOC )(.+)$')
### Line 3
CHRG_GJ_CT_REGEX = re.compile(r'(?<=GJ COURT )(.+)(?= CURRENT COURT)')
CHRG_CURR_CT_REGEX = re.compile(r'(?<=CURRENT COURT )(.+)(?= PREVIOUS COURTS)')
CHRG_PREV_CT_REGEX = re.compile(r'(?<=PREVIOUS COURTS )(.+)(?= CHOV DT)')
CHRG_CHOV_DT_REGEX = re.compile(r'(?<=CHOV DT )(.+)$')

##########################################################################
#####                             BONDS                              #####
##########################################################################
### Line 1
BOND_DATE_SET_REGEX = re.compile(r'(?<=DATE BOND SET )(.+)(?= AMT)')
BOND_AMT_REGEX = re.compile(r'(?<=AMT )(.+)(?= TYPE)')
BOND_TYPE_REGEX = re.compile(r'(?<=TYPE )(.+)(?= SET BY COURT)')
BOND_SET_BY_REGEX = re.compile(r'(?<=SET BY COURT )(.+)(?= JUDGE)')
BOND_JUDGE_REGEX = re.compile(r'(?<=JUDGE )(.+)$')
### Line 2
BOND_REC_NO_REGEX = re.compile(r'(?<=REC NO )(.+)$')

##########################################################################
#####                         DISPOSITION                            #####
##########################################################################
### Line 1
DISP_NO_REGEX = re.compile(r'(?<= CT DISP NO )(.+)$')
### Line 2
DISP_VERDICT_DATE_REGEX = re.compile(r'(?<=VERDICT DATE )(.+)(?= BY JG  DISP )')
DISP_VERDICT_BY_REGEX = re.compile(r'(?<=BY )(.+)(?= DISP )')
DISP_VERDICT_JG_REGEX = re.compile(r'(?<=JG )(.+)(?= TC)')
DISP_TC_REGEX = re.compile(r'(?<=TC )(.+)(?= DISM TYP )')
DISP_DISM_TYP_REGEX = re.compile(r'(?<=DISM TYP )(.+)(?= VOL)')
DISP_VERDICT_VOL_REGEX = re.compile(r'(?<=VOL )(.+)(?= PAGE)')
DISP_VERDICT_PAGE_REGEX = re.compile(r'(?<=PAGE )(.+)$')
### Line 3
DISP_SENT_DATE_REGEX = re.compile(r'(?<=SENTENCE DATE )(.+)(?= BY)')
DISP_SENT_BY_REGEX = re.compile(r'(?<= BY )(.+)(?= TO)')
DISP_SENT_TO_REGEX = re.compile(r'(?<=TO )(.+)(?= YEARS)')
DISP_SENT_YEARS_REGEX = re.compile(r'(?<=YEARS )(.+)(?= MTHS)')
DISP_SENT_MONTHS_REGEX = re.compile(r'(?<=MTHS )(.+)(?= DAYS)')
DISP_SENT_HOURS_REGEX = re.compile(r'(?<=HOURS )(.+)$')
### Line 4
DISP_SENT_BEGIN_REGEX = re.compile(r'(?<=SENTENCE TO BEGIN )(.+)(?= SENTENCE VOL)')
DISP_SENT_VOL_REGEX = re.compile(r'(?<=SENTENCE VOL )(.+)(?= PAGE)')
DISP_SENT_PAGE_REGEX = re.compile(r'(?<=PAGE )(.+)(?= DISCHARGE )')
DISP_DISCHARGE_REGEX = re.compile(r'(?<=DISCHARGE )(.+)(?= TYPE)')
DISP_DISCH_TYPE_REGEX = re.compile(r'(?<=TYPE )(.+)(?= NUM)')
DISP_NUM_REGEX = re.compile(r'(?<=NUM )(.+)$')
### Line 5
DISP_PROB_SENT_TO_REGEX = re.compile(r'(?<=PROBATED SENTENCE TO )(.+)(?= YEARS)')
DISP_PROB_SENT_YEARS_REGEX = re.compile(r'(?<=YEARS )(.+)(?= MONTHS)')
DISP_PROB_SENT_MONTHS_REGEX = re.compile(r'(?<=MONTHS )(.+)(?= DAYS)')
DISP_PROB_SENT_DAYS_REGEX = re.compile(r'(?<=DAYS )(.+)(?= MULT SENT)')
DISP_MULT_SENT_REGEX = re.compile(r'(?<=MULT SENT )(.+)$')
### Line 6
DISP_PROB_YEARS_REGEX = re.compile(r'(?<=PROBATED FOR  YEARS )(.+)(?= MONTHS)')
DISP_PROB_MONTHS_REGEX = re.compile(r'(?<=MONTHS )(.+)(?= DAYS)')
DISP_PROB_DAYS_REGEX = re.compile(r'(?<=DAYS )(.+)(?= PROBATION START DATE)')
DISP_PROB_START_DATE_REGEX = re.compile(r'(?<=PROBATION START DATE )(.+)$')
### Line 7
DISP_SPEC_COND_1_REGEX = re.compile(r'(?<=SPEC COND 1 )(.+)(?= FOR .+ 2)')
DISP_FOR_1_REGEX = re.compile(r'(?<=FOR )(.+)(?= 2 )')
DISP_SPEC_COND_2_REGEX = re.compile(r'(?<=2 )(.+)(?= FOR)')
DISP_FOR_2_REGEX = re.compile(r'(?<=FOR )(.+)$')
### Line 8
DISP_FINE_CODE_REGEX = re.compile(r'(?<=FINE CODE )(.+)(?= AMT .+ COST CODE)')
DISP_FINE_AMT_REGEX = re.compile(r'(?<=AMT )(.+)(?= COST CODE)')
DISP_COST_CODE_REGEX = re.compile(r'(?<=COST CODE )(.+)(?= AMT)')
DISP_COST_AMT_REGEX = re.compile(r'(?<=COST CODE .  AMT )(.+)(?= PAYMENT DUE)')
DISP_DUE_DATE_REGEX = re.compile(r'(?<=PAYMENT DUE )(.+)$')

##########################################################################
#####                   REDUCED/ENHANCED CHARGE                      #####
##########################################################################
### Line 1
RED_ENH_DESC_REGEX = re.compile(r'(?<=DESC )(.+)(?= COMT)')
RED_ENH_COMT_REGEX = re.compile(r'(?<=COMT )(.+)(?= TYP/CL)')
RED_ENH_TYP_CL_REGEX = re.compile(r'(?<=TYP/CL )(.+)(?= GOC)')
RED_ENH_GOC_REGEX = re.compile(r'(?<=GOC )(.+)$')
### Line 2
RED_ENH_COUNTY_REGEX = re.compile(r'(?<=COUNTY CODE )(.+)(?= STATE CODE)')
RED_ENH_STATE_REGEX = re.compile(r'(?<=STATE CODE )(.+)$')
### Line 3
RED_ENH_REVOC_DATE_REGEX = re.compile(r'(?<=PROBATION REVOCATION FILE DATE )(.+)(?= WARRANT ISSUED DATE)')
RED_ENH_WARR_REGEX = re.compile(r'(?<=WARRANT ISSUED DATE )(.+)$')
### Line 4:
RED_ENH_COMMENT_REGEX = re.compile(r'(?<=DISPOSITION COMMENT )(.+)$')

##########################################################################
#####                      GENERAL COMMENTS                          #####
##########################################################################
### Line 1
GC_COMMENT_REGEX = re.compile(r'(?<=C080 )(.+)$')
### Line 2
GC_DATE_REGEX = re.compile(r'(?<=DATE )(.+)$')

##########################################################################
#####                   GENERAL COMMENTS WS DATE                     #####
##########################################################################
### Line 1
GC_WS_COMMENT_REGEX = re.compile(r'(?<=B080 )(.+)(?= . [0-9]{6})')
GC_WS_COMMENT_TYPE_REGEX = re.compile(r'(?<= )(.)(?= [0-9]{6})')
GC_WS_DATE_REGEX = re.compile(r'(?<= . )([0-9]{6})(?= [0-9])')
GC_WS_EXTRA_REGEX = re.compile(r'(?<=[0-9]{6} )(.+)$')

##########################################################################
#####                           MOTIONS                              #####
##########################################################################
### Line 1
MOT_DISP_NO_REGEX = re.compile(r'(?<=CT DISP NO )(.+)$')
### Line 2
MOT_FILED_REGEX = re.compile(r'(?<=DT FILED )(.+)(?= MOTN TYPE )')
MOT_TYPE_REGEX = re.compile(r'(?<=MOTN TYPE )(.+)(?= MOTN PENDING )')
MOT_PEND_REGEX = re.compile(r'(?<=MOTN PENDING )(.+)(?= STATEMENT OF FACTS FILED )')
MOT_FACTS_REGEX = re.compile(r'(?<=STATEMENT OF FACTS FILED )(.+)$')
### Line 3
MOT_DESC_REGEX = re.compile(r'(?<=DESC )(.+)(?= SENT PENDING )')
MOT_SENT_PEND_REGEX = re.compile(r'(?<=SENT PENDING )(.+)(?= DISPOSED DT)')
MOT_DISP_DT_REGEX = re.compile(r'(?<=DISPOSED DT )(.+)(?= TYPE)')
MOT_DISP_TYPE_REGEX = re.compile(r'(?<=TYPE )(.+)$')
### Line 4
MOT_COMMENT_REGEX = re.compile(r'(?<=COMMENT )(.+)(?= REC NO )')
MOT_REC_NO_REGEX = re.compile(r'(?<=REC NO )(.+)$')

##########################################################################
#####                    PROBATION REVOCATION                        #####
##########################################################################
### Line 1
PROB_NO_REGEX = re.compile(r'(?<=CT DISP NO )(.+)$')
### Line 2
PROB_VERDICT_DATE_REGEX = re.compile(r'(?<=VERDICT DATE )(.+)(?= BY JG  DISP )')
PROB_VERDICT_BY_REGEX = re.compile(r'(?<=BY )(.+)(?= DISP )')
PROB_VERDICT_JG_REGEX = re.compile(r'(?<=JG )(.+)(?= TC)')
PROB_TC_REGEX = re.compile(r'(?<=TC )(.+)(?= DISM TYP )')
PROB_DISM_TYP_REGEX = re.compile(r'(?<=DISM TYP )(.+)(?= VOL)')
PROB_VERDICT_VOL_REGEX = re.compile(r'(?<=VOL )(.+)(?= PAGE)')
PROB_VERDICT_PAGE_REGEX = re.compile(r'(?<=PAGE )(.+)$')
### Line 3
PROB_SENT_DATE_REGEX = re.compile(r'(?<=SENTENCE DATE )(.+)(?= BY)')
PROB_SENT_BY_REGEX = re.compile(r'(?<= BY )(.+)(?= TO)')
PROB_SENT_TO_REGEX = re.compile(r'(?<=TO )(.+)(?= YEARS)')
PROB_SENT_YEARS_REGEX = re.compile(r'(?<=YEARS )(.+)(?= MTHS)')
PROB_SENT_MONTHS_REGEX = re.compile(r'(?<=MTHS )(.+)(?= DAYS)')
PROB_SENT_DAYS_REGEX = re.compile(r'(?<=DAYS )(.+)(?= HOURS)')
PROB_SENT_HOURS_REGEX = re.compile(r'(?<=HOURS )(.+)$')
### Line 4
PROB_SENT_BEGIN_REGEX = re.compile(r'(?<=SENTENCE TO BEGIN )(.+)(?= SENTENCE VOL)')
PROB_SENT_VOL_REGEX = re.compile(r'(?<=SENTENCE VOL )(.+)(?= PAGE)')
PROB_SENT_PAGE_REGEX = re.compile(r'(?<=PAGE )(.+)(?= DISCHARGE )')
PROB_DISCHARGE_REGEX = re.compile(r'(?<=DISCHARGE )(.+)(?= TYPE)')
PROB_DISCH_TYPE_REGEX = re.compile(r'(?<=TYPE )(.+)(?= NUM)')
PROB_NUM_REGEX = re.compile(r'(?<=NUM )(.+)$')
### Line 5
PROB_PROB_SENT_TO_REGEX = re.compile(r'(?<=PROBATED SENTENCE TO )(.+)(?= YEARS)')
PROB_PROB_SENT_YEARS_REGEX = re.compile(r'(?<=YEARS )(.+)(?= MONTHS)')
PROB_PROB_SENT_MONTHS_REGEX = re.compile(r'(?<=MONTHS )(.+)(?= DAYS)')
PROB_PROB_SENT_DAYS_REGEX = re.compile(r'(?<=DAYS )(.+)(?= MULT SENT)')
PROB_MULT_SENT_REGEX = re.compile(r'(?<=MULT SENT )(.+)$')
### Line 6
PROB_PROB_YEARS_REGEX = re.compile(r'(?<=PROBATED FOR  YEARS )(.+)(?= MONTHS)')
PROB_PROB_MONTHS_REGEX = re.compile(r'(?<=MONTHS )(.+)(?= DAYS)')
PROB_PROB_DAYS_REGEX = re.compile(r'(?<=DAYS )(.+)(?= PROBATION START DATE)')
PROB_PROB_START_DATE_REGEX = re.compile(r'(?<=PROBATION START DATE )(.+)$')
### Line 7
PROB_SPEC_COND_1_REGEX = re.compile(r'(?<=SPEC COND 1 )(.+)(?= FOR .+ 2)')
PROB_FOR_1_REGEX = re.compile(r'(?<=FOR )(.+)(?= 2 )')
PROB_SPEC_COND_2_REGEX = re.compile(r'(?<=2 )(.+)(?= FOR)')
PROB_FOR_2_REGEX = re.compile(r'(?<=FOR )(.+)$')
### Line 8
PROB_FINE_CODE_REGEX = re.compile(r'(?<=FINE CODE )(.+)(?= AMT .+ COST CODE)')
PROB_FINE_AMT_REGEX = re.compile(r'(?<=AMT )(.+)(?= COST CODE)')
PROB_COST_CODE_REGEX = re.compile(r'(?<=COST CODE )(.+)(?= AMT)')
PROB_COST_AMT_REGEX = re.compile(r'(?<=COST CODE .  AMT )(.+)(?= PAYMENT DUE)')
PROB_DUE_DATE_REGEX = re.compile(r'(?<=PAYMENT DUE )(.+)$')

##########################################################################
#####                           APPEALS                              #####
##########################################################################
### Line 1
APPL_NO_REGEX = re.compile(r'(?<=CT DISP NO )(.+)$')
### Line 2
APPL_DATE_REGEX = re.compile(r'(?<=DATE APPEAL MADE )(.+)(?= COPY STATEMENT OF FACTS FILED)')
APPL_FILE_REGEX = re.compile(r'(?<=COPY STATEMENT OF FACTS FILED )(.+)(?= EXTENDED)')
APPL_EXT_REGEX = re.compile(r'(?<=EXTENDED )(.+)$')
### Line 3
APPL_DESIG_REGEX = re.compile(r'(?<=DESIGNATION OF RECORD  DEFENSE )(.+)(?= STATE)')
APPL_STATE_REGEX = re.compile(r'(?<=STATE )(.+)(?= TRANSCRIPT FILED)')
APPL_TRANS_REGEX = re.compile(r'(?<=TRANSCRIPT FILED )(.+)$')
### Line 4
APPL_OBJ_REGEX = re.compile(r'(?<=OBJECTION )(.+)(?= DATE NOTICE SENT)')
APPL_NOT_REGEX = re.compile(r'(?<=DATE NOTICE SENT )(.+)$')
### Line 5
APPL_DATE_SENT_REGEX = re.compile(r'(?<=DATE SENT TO APPEALS )(.+)(?= OPINION DATE)')
APPL_OPINION_REGEX = re.compile(r'(?<=OPINION DATE )(.+)(?= MANDATE RECEIVED)')
APPL_MAND_REC_REGEX = re.compile(r'(?<=MANDATE RECEIVED )(.+)(?= DISP )')
APPL_DISP_REGEX = re.compile(r'(?<=DISP )(.+)$')
### Line 6
APPL_MAND_ENF_REGEX = re.compile(r'(?<=MANDATE ENFORCED DATE )(.+)(?= APPEAL WITHDRAWN)')
APPL_WITH_REGEX = re.compile(r'(?<=APPEAL WITHDRAWN )(.+)(?= CT REPORTER INITIALS )')
APPL_REPORTER_REGEX = re.compile(r'(?<=CT REPORTER INITIALS )(.+)$')
### Line 7
APPL_REF_CODE_REGEX = re.compile(r'(?<=APPEAL REF CODE )(.+)(?= REC NO )')
APPL_REC_NO_REGEX = re.compile(r'(?<=REC NO )(.+)$')

##########################################################################
#####                     COMPETENCY DATA                            #####
##########################################################################
### Line 1
COMP_DATE_REGEX = re.compile(r'(?<=HEARING DATE )(.+)(?= PURPOSE)')
COMP_PURP_REGEX = re.compile(r'(?<=PURPOSE )(.+)(?= RESULT)')
COMP_RESULT_REGEX = re.compile(r'(?<=RESULT )(.+)(?= FINDING BY)')
COMP_FIND_REGEX = re.compile(r'(?<=FINDING BY )(.+)$')
### Line 2
COMP_COMMENT_REGEX = re.compile(r'(?<=COMMENT )(.+)(?= REC NO)')
COMP_REC_NO_REGEX = re.compile(r'(?<=REC NO )(.+)$')

##########################################################################
#####                         PAYMENTS                               #####
##########################################################################
### Line 1
PAY_DISP_NO_REGEX = re.compile(r'(?<=CT DISP NO )(.+)$')
### Line 2
PAY_DATE_REGEX = re.compile(r'(?<=DATE PAID )(.+)(?= AMT PAID)')
PAY_AMT_REGEX = re.compile(r'(?<=AMT PAID )(.+)(?= TYPE PAYMENT)')
PAY_TYPE_REGEX = re.compile(r'(?<=TYPE PAYMENT )(.+)(?= RECEIPT NO)')
PAY_RECEIPT_REGEX = re.compile(r'(?<=RECEIPT NO )(.+)$')
### Line 3
PAY_RECD_BY_REGEX = re.compile(r"(?<=REC'D BY )(.+)(?= PD UP)")
PAY_PD_UP_REGEX = re.compile(r'(?<=PD UP )(.+)(?= DATE NEXT PAYMENT)')
PAY_NEXT_DT_REGEX = re.compile(r'(?<=DATE NEXT PAYMENT )(.+)(?= AMT NEXT PAYMENT)')
PAY_NEXT_AMT_REGEX = re.compile(r'(?<=AMT NEXT PAYMENT )(.+)$')
### Line 4
PAY_REC_NO_REGEX = re.compile(r'(?<=REC NO )(.+)$')

##########################################################################
#####                      BOND COMMENTS                             #####
##########################################################################
### Line 1
BC_DATE_REGEX = re.compile(r'(?<=DATE )([0-9]{6})')
### Line 2
BC_COMMENT_REGEX = re.compile(r'(.+)(?= FUNC )')
BC_FUNC_REGEX = re.compile(r'(?<= FUNC )(.+)$')
