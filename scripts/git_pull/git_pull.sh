#!/bin/bash - 
#===============================================================================
#
#          FILE: git_pull.sh
# 
#         USAGE: ./git_pull.sh 
# 
#   DESCRIPTION: 
#
# Script qui "git pull" sur un serveur web.
# il est destiné à etre utilisé avec ssh.                
# il prend en option le nom du site web sur lequel effectuer le pull.  
#               
# 
#       OPTIONS: -s name_site_web
#  REQUIREMENTS: git ssh
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Barattero Laurent 
#  ORGANIZATION: 
#       CREATED: 25/05/2013 06:33:15 CEST
#      REVISION: 0.0
#===============================================================================

set -o nounset                              # Treat unset variables as an error

# Parametres
#===========
# tableau qui contient les sites valides
site=("site1" "site2" "site3" "siter41")
# 1) Site 1
laurent_site_path="$HOME/path/to/site"
# 2) Site 2
lub_site_path="$HOME/path/to/site"
# 3) Site 3
# ...

opt_site=""

while getopts ":s:" opt ; do
    case $opt in
        s ) opt_site=$OPTARG
            ;;
        ? ) echo 'usage : git_fetch [-s site_name]'
            exit 1
    esac    
done

# l'option -s est obligatoire
if [[ -z $opt_site ]]; then
    echo "la cible (site) n'est pas defini."
    echo "--> l'option -s site_name est obligatoire"
    exit 1
fi

# verification, pour voir si le nom du site est valide 
#-----------------------------------------------------
is_valid_site=0
for  i in ${site[*]} ; do
    if [ $i == $opt_site ]; then
        is_valid_site=1
    fi
done
# si il n'est pas valide sort du script
if [ $is_valid_site -eq 0 ]; 
then
    echo "Le site \""$opt_site"\" n'est pas valide." 
    echo "Les sites enregistré sont :" 
    for  i in ${site[*]} ; do
        echo -e "\t-> "$i
    done
    exit 1
fi

# functions utilitaires

function title_h1 ()
{
    echo $1
    printf -v line '%*s' "${#1}"
    echo ${line// /=}
    echo
}	# ----------  end of function underline  ----------


###############################
# Execution des taches utiles #
###############################

bando_site="Site sélectionné : $opt_site"
title_h1 "$bando_site"
echo 
#git_target=${opt_site}"_git_target"
site_path=${opt_site}"_site_path"

cd ${!site_path}
git pull origin
 

