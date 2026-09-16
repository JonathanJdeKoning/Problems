class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        myEn = initialEnergy
        myEx = initialExperience

        moreEn = 0
        moreEx = 0
        for i in range(len(energy)):
            opEn = energy[i]
            opEx = experience[i]

            if opEn >= myEn:
                bump = (opEn-myEn)+1
                myEn += bump
                moreEn += bump
                myEn -= opEn
            else:
                myEn -= opEn
            
            if opEx >= myEx:
                bump = (opEx-myEx) + 1
                myEx += bump
                moreEx += bump
                myEx += opEx
            else:
                myEx += opEx
        return moreEn+moreEx