# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: soraya <soraya@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/13 14:35:14 by soraya              #+#    #+#            #
#   Updated: 2026/02/13 15:02:56 by soraya             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    a = int(input("Day 1 harvest: "))
    b = int(input("Day 2 harvest: "))
    c = int(input("Day 3 harvest: "))
    total = a + b + c
    print("Total harvest:", total)
