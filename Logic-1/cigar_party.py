def cigar_party(cigars, is_weekend):
    if is_weekend is False and cigars >= 40 and cigars <= 60:
        return True
    elif is_weekend is True and cigars >= 40:
        return True
    return False

  #   def cigar_party(cigars, is_weekend):
  # if is_weekend:
  #   return (cigars >= 40)
  # else:
  #   return (cigars >= 40 and cigars <= 60)
