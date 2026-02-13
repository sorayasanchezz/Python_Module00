# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: soraya <soraya@student.42.fr>                +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/02/13 17:05:36 by soraya              #+#    #+#            #
#   Updated: 2026/02/13 17:28:43 by soraya             ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(start, end):
        if (start > end):
            print("Harvest time!")
            return
        print(f"Day {start}")
        count(start + 1, end)

    count(1, days)
