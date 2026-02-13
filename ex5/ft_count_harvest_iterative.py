# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#    ft_count_harvest_iterative.py                       :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: soraya <soraya@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/13 16:49:09 by soraya              #+#    #+#            #
#   Updated: 2026/02/13 17:05:22 by soraya             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
