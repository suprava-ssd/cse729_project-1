from InputsConfig import InputsConfig as p
from Models.Consensus import Consensus as c

class Incentives:
    HALVING_INTERVAL = 40
    """
	 Defines the rewarded elements (block + transactions), calculate and distribute the rewards among the participating nodes
    """
    def distribute_rewards():
            for bc in c.global_chain:
                for m in p.NODES:
                    if bc.miner == m.id:
                        m.blocks +=1
                        number_of_halvings = bc.depth // Incentives.HALVING_INTERVAL
                        current_reward = p.Breward / (2 ** number_of_halvings)
                        m.balance += current_reward
                        tx_fee= Incentives.transactions_fee(bc)
                        m.balance += tx_fee


    def transactions_fee(bc):
        fee=0
        for tx in  bc.transactions:
            fee += tx.fee
        return fee
