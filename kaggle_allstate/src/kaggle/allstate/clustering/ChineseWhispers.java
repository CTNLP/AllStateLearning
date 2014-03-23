/**
 * 
 */
package kaggle.allstate.clustering;

import it.unimi.dsi.fastutil.ints.Int2DoubleOpenHashMap;
import it.unimi.dsi.fastutil.ints.Int2IntOpenHashMap;
import it.unimi.dsi.fastutil.ints.Int2ObjectOpenHashMap;
import it.unimi.dsi.fastutil.ints.IntIterator;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;
import kaggle.allstate.datastructures.DataSet;
import kaggle.allstate.datastructures.SingleCostumer;

/**
 * @author Christoph Teichmann
 * created Mar 23, 2014 12:20:43 PM
 * @version 0.1
 */
public class ChineseWhispers
{
	/**
	 * 
	 */
	private final int iterations;
	/**
	 * 
	 * @param maxConnections
	 * @param weights
	 * @param es
	 */
	public ChineseWhispers(int maxConnections, int iterations, double[][] weights, double[][] es)
	{
		this.maxConnections = maxConnections;
		this.iterations = iterations;
		this.weights = weights;
		this.es = es;
	}
	/**
	 * 
	 */
	private final int maxConnections;
	/**
	 * 
	 */
	private final double[][] weights;
	/**
	 * 
	 */
	private final double[][] es;
	/**
	 * 
	 *
	 * @return
	 */
	public ArrayList<Set<SingleCostumer>> cluster(DataSet data)
	{
		Int2ObjectOpenHashMap<Int2DoubleOpenHashMap> incomingConnections = makeIncomingConnections(data);
		Int2IntOpenHashMap clusterAssignments = makeAssignments(incomingConnections);
		return transformToSets(clusterAssignments, data);
	}
	/**
	 *
	 * @param clusterAssignments
	 * @return
	 */
	private ArrayList<Set<SingleCostumer>> transformToSets(
			Int2IntOpenHashMap clusterAssignments, DataSet data)
	{
		Int2ObjectOpenHashMap<Set<SingleCostumer>> map = new Int2ObjectOpenHashMap<Set<SingleCostumer>>();
		IntIterator iit = clusterAssignments.keySet().iterator();
		while(iit.hasNext())
		{
			int costumer = iit.nextInt();
			int cluster = clusterAssignments.get(costumer);
			Set<SingleCostumer> s = map.get(cluster);
			if(s == null)
			{
				s = new HashSet<>();
				map.put(cluster, s);
			}
			s.add(data.get(costumer));
		}
		ArrayList<Set<SingleCostumer>> list = new ArrayList<>();
		for(Set<SingleCostumer> set : map.values())
		{list.add(set);}
		return list;
	}
	/**
	 *
	 * @param incomingConnections
	 * @return
	 */
	private Int2IntOpenHashMap makeAssignments(
			Int2ObjectOpenHashMap<Int2DoubleOpenHashMap> incomingConnections)
	{
		IntIterator iit = incomingConnections.keySet().iterator();
		Int2IntOpenHashMap result = new Int2IntOpenHashMap();
		while(iit.hasNext())
		{
			int num = iit.nextInt();
			result.put(num, num);
		}
		Int2DoubleOpenHashMap clusterWeights = new Int2DoubleOpenHashMap();
		for(int i=0;i<this.iterations;++i)
		{
			iit = incomingConnections.keySet().iterator();
			while(iit.hasNext())
			{
				int node = iit.nextInt();
				Int2DoubleOpenHashMap map = incomingConnections.get(node);
				clusterWeights.clear();
				IntIterator q = map.keySet().iterator();
				while(q.hasNext())
				{
					int other = q.nextInt();
					clusterWeights.addTo(result.get(other), clusterWeights.get(other));
				}
				result.put(node, selectBest(clusterWeights));
			}
		}
		return result;
	}
	/**
	 *
	 * @param clusterWeights
	 * @return
	 */
	private int selectBest(Int2DoubleOpenHashMap clusterWeights)
	{
		int best = -1;
		double bestWeight = Double.NEGATIVE_INFINITY;
		IntIterator iit = clusterWeights.keySet().iterator();
		while(iit.hasNext())
		{
			int cand = iit.nextInt();
			double w = clusterWeights.get(cand);
			if( w > bestWeight)
			{
				bestWeight = w;
				best = cand;
			}
		}
		return best;
	}
	/**
	 *
	 * @param data 
	 * @return
	 */
	private Int2ObjectOpenHashMap<Int2DoubleOpenHashMap> makeIncomingConnections(DataSet data)
	{
		PriorityPair pp = new PriorityPair();
		PriorityQueue<PriorityPair> queue = new PriorityQueue<>();
		IntIterator first = data.getIntIterator();
		Int2ObjectOpenHashMap<Int2DoubleOpenHashMap> ret = new Int2ObjectOpenHashMap<>();
		while(first.hasNext())
		{
			int a = first.nextInt();
			IntIterator second = data.getIntIterator();
			SingleCostumer sc = data.get(a);
			queue.clear();
			while(second.hasNext())
			{
				int b = second.nextInt();
				if(a==b)
				{continue;}
				SingleCostumer other = data.get(b);
				double nearness = sc.rdf(other, 0, sc.size(), weights, es);
				if(queue.size() < this.maxConnections)
				{
					PriorityPair p = new PriorityPair();
					p.key = nearness;
					p.value = b;
					queue.add(p);
				}
				else
				{
					pp.key = nearness;
					pp.value = b;
					queue.add(pp);
					pp = queue.poll();
				}
			}
			Int2DoubleOpenHashMap m = new Int2DoubleOpenHashMap();
			while(!queue.isEmpty())
			{
				PriorityPair s = queue.poll();
				m.put(s.value, s.key);
			}
			ret.put(a, m);
		}
		return ret;
	}
	/**
	 * 
	 * @author Christoph Teichmann
	 * created Mar 23, 2014 6:49:02 PM
	 * @version 0.1
	 */
	private class PriorityPair implements Comparable<PriorityPair>
	{
		/**
		 * 
		 */
		private int value;
		/**
		 * 
		 */
		private double key;
		/* (non-Javadoc)
		 * @see java.lang.Comparable#compareTo(java.lang.Object)
		 */
		@Override
		public int compareTo(PriorityPair o)
		{return Double.compare(key, o.key);}
	}
}