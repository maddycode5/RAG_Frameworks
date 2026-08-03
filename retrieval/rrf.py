"""
Purpose:
    Implements Reciprocal Rank Fusion (RRF) for combining
    multiple ranked retrieval results.

Formula:

            1
-------------------------
k + rank(position)

Final Score = Σ (1 / (k + rank))

"""

from collections import defaultdict
from typing import List

from core.retrieval_result import RetrievalResult

class ReciprocalRankFusion:

    def __init__(self,k:int =60):
        """
        Parameters 

        k : int 
        - contant used in RRF formula
        - Recommended value = 60
        """
        self.k = k

    def fuse(
            self,
            *rankings :List[RetrievalResult]        
        )->List[RetrievalResult]:
        """
        Fuse multiple ranked lists into one

        parameters 
        ranking  :
            multiple retrievalresult list

        returns 
        list[retrievalResult]
        """
        fused_scores =defaultdict(float)
        result_lookup= []

        # compute the RRF SCORE
        for ranking in rankings:
            for rank,result in enumerate(ranking,start=1):
                chunk_id = result.chunk.chunk_id
                fused_scores[chunk_id] += 1 / (self.k + rank)

                result_lookup[chunk_id] = result 

        # sort by RRF SCORE

        sorted_results = sorted(
            fused_scores.items(),
            key=lambda x:x[1],
            reverse = True, 
        )

        fused_results = []

        for final_rank ,(chunk_id,score) in enumerate(sorted_results,start = 1,):
            result =result_lookup[chunk_id]

            # create the metadata dictionary if t does not exist
            if result.metadata is None:
                result.metadata = {}

            # preserve previous score
            result.metadata["rrf_score"] =score

            # update result 
            result.score=score
            result.rank = final_rank
            result.source ="hybrid"
            fused_results.append(result)


            result.metadata["original_Score"] = result.score
            result.metadata["rrf_score"] = score
            
        return fused_results

        