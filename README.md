# General Place Recognition Survey: Towards Real-World Autonomy

<!-- <p align="center">
  <img src="https://github.com/ContinualAI/continual-learning-papers/blob/main/logo.png" alt="ContinualAI logo"/ width="300px" align="center">
</p> -->

<!-- Continual Learning papers list, curated by ContinualAI. **Search among 325 papers!**
 
You can browse the list in this file or interactively on the [ContinualAI website](https://www.continualai.org/papers/).

[Join our community](https://continualai.herokuapp.com/) on Slack to stay updated with the latest Continual Learning news.  
Visit the Continua AI wiki &rarr; http://wiki.continualai.org/ -->

General Place Recognition papers list. **Search among 170 papers!**

## Table of contents
<!-- [Add a new paper](https://github.com/ContinualAI/continual-learning-papers#add-a-new-paper)   -->
<!-- [Join the ContinualAI Zotero group](https://github.com/ContinualAI/continual-learning-papers#join-the-continualai-zotero-group)   -->
* [List of papers]()
    - [Review paper](#review-papers)
    - [Representation](#representation)
      - [Camera-Related Approaches (VPR)](#camera-related-approaches)
      - [Range Sensor-Related Approaches (LPR/RPR)](#range-sensor-related-approaches)
    - [Recognizing the Right Place Aginst Challenges](#recognizing-the-right-place-aginst-challenges)
      - [Appearance Change](#a-appearance-change)
      - [Viewpoint Difference](#b-viewpoint-difference)
      - [Generalization Ability](#c-generalization-ability)
      - [Efficiency](#d-efficiency)
      - [Uncertainty Estimation](#e-uncertainty-estimation)
    - [Application and Trends](#application--trends)
      - [Large-Scale and Long-Term Navigation](#a-long-term--large-scale-navigation)
      - [Visual Relative Terrain Navigation](#b-visual-terrain-relative-navigation)
      - [Multi-Agent Localization and Mapping](#c-multi-agent-localization-and-mapping)
      - [Bio-Inspired and Lifelong Autonomy](#d-bio-inspired-and-lifelong-autonomy)
    - [Development Tools](#development-tools)
      - [Public Datasets](#a-public-datasets)
      - [Open Libraries](#b-supported-libraries)

---------------------------------------------------

## Existing Datasets

| Topic             | Name                                                         | Year | Image type      | Environment     | Illumination       | Viewpoint          | Ground Truth       | Labels             | Extra Information |
| ----------------- | ------------------------------------------------------------ | ---- | --------------- | --------------- | ------------------ | ------------------ | ------------------ | ------------------ | ----------------- |
| Generic           | [New College and City Centre](http://www.robots.ox.ac.uk/~mobile/IJRR_2008_Dataset/data.html)| 2008 | RGB             | Outdoor         | slight             | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | GPS               |
|                   | [New College Vision and Laser ](https://ori.ox.ac.uk/older-projects/new-college-dataset/) | 2009 | Gray\.          | Outdoor         | slight             | :heavy_check_mark: | :heavy_check_mark: |                    | GPS, IMU, LiDAR   |
|                   | [Rawseeds](http://www.rawseeds.org/home/)                    | 2006 | RGB             | Indoor/Outdoor  |                    | :heavy_check_mark: | :heavy_check_mark: |                    | GPS, LiDAR        |
|                   | [Ford Campus](http://robots.engin.umich.edu/SoftwareData/Ford) | 2011 | RGB             | Urban           | slight             |                    | :heavy_check_mark: |                    | GPS, IMU, LiDAR   |
|                   | [Malaga Parking 6L](https://www.mrpt.org/malaga_dataset_2009) | 2009 | RGB             | Outdoor         |                    |                    | :heavy_check_mark: |                    | GPS, IMU, LiDAR   |
|                   | [KITTI Odometry](http://www.cvlibs.net/datasets/kitti/eval_odometry.php) | 2012 | Gray\./ RGB     | Urban           | slight             |                    | :heavy_check_mark: |                    | GPS, IMU, LiDAR   |
| Long\-term        | [St\. Lucia](https://wiki.qut.edu.au/display/cyphy/St+Lucia+Multiple+Times+of+Day) | 2010 | RGB             | Urban           | :heavy_check_mark: | slight             |                    |                    | GPS               |
|                   | [COLD](https://www.nada.kth.se/cas/COLD/)                    | 2009 | RGB             | Indoor          | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | LiDAR             |
|                   | [Oxford RobotCar](https://robotcar-dataset.robots.ox.ac.uk/) | 2017 | RGB             | Urban           | :heavy_check_mark: |                    | :heavy_check_mark: |                    | GPS, IMU, LiDAR   |
|                   | [Gardens Point Walking](https://goo.gl/tqmWyq)               | 2014 | RGB             | Indoor/ Outdoor | :heavy_check_mark: | :heavy_check_mark: |                    |                    | \-                |
|                   | [MSLS](https://www.mapillary.com/dataset/places)             | 2020 | RGB             | Urban           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | GPS               |
| Across seasons    | [Nurburgring and Alderley](https://wiki.qut.edu.au/display/cyphy/Michael+Milford+Datasets+and+Downloads) | 2012 | RGB             | Urban           | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: | \-                |
|                   | [Nordland](https://nrkbeta.no/2013/01/15/)                   | 2013 | RGB             | Outdoor         | :heavy_check_mark: |                    | :heavy_check_mark: |                    | GPS               |
|                   | [CMU](http://3dvis.ri.cmu.edu/data-sets/localization/)       | 2011 | RGB             | Urban           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | GPS               |
|                   | [Freiburg \(FAS\)](http://aisdatasets.informatik.uni-freiburg.de/freiburg_across_seasons/) | 2014 | RGB             | Urban           | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: | GPS               |
|                   | [VPRiCE](https://goo.gl/R0QYU2)                              | 2015 | RGB             | Outdoor         | :heavy_check_mark: | :heavy_check_mark: |                    |                    | \-                |
| RGB\-D            | [TUM RGB\-D](https://vision.in.tum.de/data/datasets/rgbd-dataset) | 2012 | RGB\-D          | Indoor          |                    | :heavy_check_mark: | :heavy_check_mark: |                    | IMU               |
|                   | [Microsoft 7\-Scenes](https://www.microsoft.com/en-us/research/project/rgb-d-dataset-7-scenes/) | 2013 | RGB\-D          | Indoor          |                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | \-                |
|                   | [ICL\-NUIM](https://www.doc.ic.ac.uk/~ahanda/VaFRIC/iclnuim.html) | 2014 | RGB\-D          | Indoor          |                    | :heavy_check_mark: | :heavy_check_mark: |                    | \-                |
| Semantic          | [KITTI Semantic](http://www.cvlibs.net/datasets/kitti/eval_semantics.php) | 2019 | RGB             | Urban           |                    |                    | :heavy_check_mark: | :heavy_check_mark: | GPS, IMU, LiDAR   |
|                   | [Cityscapes](https://www.cityscapes-dataset.com/)            | 2016 | RGB             | Urban           |                    |                    | :heavy_check_mark: | :heavy_check_mark: | GPS               |
|                   | [CSC](https://www.visuallocalization.net/datasets/)          | 2019 | RGB             | Outdoor         | :heavy_check_mark: |                    | :heavy_check_mark: |                    | LiDAR             |
| Train networks    | [Cambridge Landmarks](http://mi.eng.cam.ac.uk/projects/relocalisation/#dataset) | 2015 | RGB             | Outdoor         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | \-                |
|                   | [Pittsburgh250k](http://www.ok.ctrl.titech.ac.jp/~torii/project/repttile/) | 2013 | RGB             | Urban           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: | GPS               |
|                   | [Tokyo 24/7](http://www.ok.ctrl.titech.ac.jp/~torii/project/247/) | 2015 | RGB             | Urban           | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | GPS               |
|                   | [SPED](https://goo.gl/OXeL2X)                                | 2017 | RGB             | Outdoor         | :heavy_check_mark: | :heavy_check_mark: |                    |                    | \-                |
| Omni\-directional | [New College Vision and Laser](https://ori.ox.ac.uk/older-projects/new-college-dataset/) | 2009 | Gray\.          | Outdoor         | slight             | :heavy_check_mark: | :heavy_check_mark: |                    | GPS, IMU, LiDAR   |
|                   | [MOLP](http://hcr.mines.edu/code/MOLP.html)                  | 2018 | Gray\./D        | Outdoor         | :heavy_check_mark: |                    | :heavy_check_mark: |                    | GPS               |
|                   | [NCLT](http://robots.engin.umich.edu/nclt/)                  | 2016 | RGB             | Outdoor         | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |                    | GPS, LiDAR        |
| Aerial/UAV        | [Shopping Street 1/2](http://www.v4rl.ethz.ch/research/datasets-code.htmls) | 2018 | Gray\.          | Urban           | slight             | :heavy_check_mark: | :heavy_check_mark: |                    | \-                |
|                   | [EuRoC](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdataset) | 2016 | Gray\.          | Indoor          |                    | :heavy_check_mark: | :heavy_check_mark: |                    | IMU               |
| Underwater        | [UWSim](https://goo.gl/GtMQkv)                               | 2016 | RGB             | Under\-water    |                    |                    | :heavy_check_mark: |                    | GPS               |
| Range sensors     | [MulRan](https://sites.google.com/view/mulran-pr)            | 2020 | 3D Point clouds | Urban           | :heavy_check_mark: |                    | :heavy_check_mark: |                    | LiDAR, RADAR      |


<!-- ## Add a new paper
The list of papers is maintained through a Zotero group. You can join the group and help us keeping it updated (see next section).  

If you don't want to join the group, you can simply open a Github issue to suggest us a new paper (or even more than one). We will take care of adding it to the list as soon as possible. 

1. Open a new Github issue.

2. Attach your bib file containing the paper you want to include in the list. If you don't have a bib file, just provide us with the link to the paper. The link should point to a location where paper metadata can be appropriately retrieved by common reference managers.

Alternatively, you can submit a Pull Request with a modification to the bibtex files directly!

## Join the ContinualAI Zotero group

You can give your contribution to the group by **adding new papers** or by helping **annotating the existing ones**.

1. Join our [Zotero group](https://www.zotero.org/groups/2623909/continual_learning_papers/)

2. To **add a new paper**

	2.1. Add it to the group folder which best represents the paper contribution. Read some advices below if you are uncertain on this. You can add the paper from your library or directly from the paper webpage through the Zotero web browser plugin. 
    
    2.2 Make sure that at least `title`, `authors`, `item type` and `publication` are specified. The `year` must be put inside `date` field.
    
    2.3 Also put a link to the paper in the `url` field. 

3. To **annotate** an existing paper

	3.1. Check the list of existing tags in `tags.csv` file. If you want to add a new tag, please add it in there and submit a Pull Request.

	3.2. Add your tags in the `Tags` tab of Zotero. Please, remember to write the tag in square brackets e.g. `[mytag]`

	3.3. Add your notes in the `Notes` tab of Zotero.

We will periodically export the bibtex to keep the list updated. In case we forgot, join the [ContinualAI Slack](https://continualai.herokuapp.com/) and complain about our behavior in the `#wiki` channel.

### Advices to add new papers in Zotero

* Check if the paper already exist by using the `Citation Key` or the title in Zotero search bar.

* Don't forget to add the publication venue (Journal, Proceedings...). Use `publication = arXiv` if the paper is a preprint.

* We use a system based on categories. This can sometimes be limiting. In general, please consider to add the paper in the category which you consider the most relevant one. You can add the paper in at most **2** categories, if you believe that both are equally relevant.

* Please, do not add new tags if a similar category already exists.

---------------------------- -->

<!-- # List of papers -->

<a id="review_paper"></a>
# Review Papers
  * S. Lowry, N. S underhauf, P. Newman, J. J. Leonard, D. Cox, P. Corke,and M. J. Milford, Visual place recognition: A survey, IEEE Transactions on robotics, vol. 32, no. 1, pp. 1–19, 2015.
  * X. Zhang, L. Wang, and Y. Su, Visual place recognition: A surveyfrom deep learning perspective, Pattern Recognition, vol. 113, p.107760, 2021.
  * S. Garg, T. Fischer, and M. Milford, Where is your place, visual placerecognition? arXiv preprint arXiv:2103.06443, 2021.
  * M. Zaffar, S. Garg, M. Milford, J. Kooij, D. Flynn, K. McDonald-Maier, and S. Ehsan, Vpr-bench: An open-source visual place recogni-tion evaluation framework with quantifiable viewpoint and appearancechange, Int. J. Comput. Vision, vol. 129, no. 7, pp. 2136–2174, jul2021.
  * J. Miao, K. Jiang, T. Wen, Y. Wang, P. Jia, X. Zhao, Z. Xiao, J. Huang,Z. Zhong, and D. Yang, A survey on monocular re-localization:From the perspective of scene map representation, arXiv preprintarXiv:2311.15643, 2023.
  * H. Yin, X. Xu, S. Lu, X. Chen, R. Xiong, S. Shen, C. Stachniss, and Y. Wang, A survey on global lidar localization: Challenges, advancesand open problems, arXiv preprint arXiv:2302.07433, 2023.

<a id="representation"></a>
# Representation

## Low-Level Representation
<a id="camera_based_approach"></a>
### Camera-Related Approaches 
  * M. Zaffar, S. Ehsan, M. Milford, and K. McDonald-Maier, Co-hog: A light-weight, compute-efficient, and training-free visual placerecognition technique for changing environments, IEEE Robotics andAutomation Letters, vol. 5, no. 2, pp. 1835–1842, 2020.
  * D. Galvez-Lopez and J. D. Tardos, Bags of binary words for fastplace recognition in image sequences, IEEE Transactions on Robotics,vol. 28, no. 5, pp. 1188–1197, 2012.
  * D. Scaramuzza, Omnidirectional Camera. Boston, MA: Springer US,2014, pp. 552–560.
  * J. Jiao, H. Wei, T. Hu, X. Hu, Y. Zhu, Z. He, J. Wu, J. Yu,X. Xie, H. Huang et al., Fusionportable: A multi-sensor campus-scenedataset for evaluation of localization and mapping accuracy on diverseplatforms, in 2022 IEEE/RSJ International Conference on IntelligentRobots and Systems (IROS). IEEE, 2022, pp. 3851–3856.
  * X. Chen, T. L ¨abe, A. Milioto, T. R ¨ohling, O. Vysotska, A. Haag,J. Behley, and C. Stachniss, Overlapnet: Loop closing for lidar-basedSLAM, CoRR, vol. abs/2105.11344, 2021.
  * Z. Hong, Y. Petillot, A. Wallace, and S. Wang, Radarslam: A robustsimultaneous localization and mapping system for all weather condi-tions, The International Journal of Robotics Research, vol. 41, no. 5,pp. 519–542, 2022.
  * R. Arandjelovic, P. Gronat, A. Torii, T. Pajdla, and J. Sivic, Netvlad:Cnn architecture for weakly supervised place recognition, in 2016IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 5297–5307.
  * G. Tolias, R. Sicre, and H. Jegou, Particular object retrieval with inte-gral max-pooling of cnn activations, arXiv preprint arXiv:1511.05879,2015.
  * F. Radenovic, G. Tolias, and O. Chum, Fine-tuning cnn image retrievalwith no human annotation, IEEE transactions on pattern analysis andmachine intelligence, vol. 41, no. 7, pp. 1655–1668, 2018.
  * G. Berton, C. Masone, and B. Caputo, Rethinking visual geo-localization for large-scale applications, in Proceedings of theIEEE/CVF Conference on Computer Vision and Pattern Recognition,2022, pp. 4878–4888.
  * R. Wang, Y. Shen, W. Zuo, S. Zhou, and N. Zheng, Transvpr:Transformer-based place recognition with multi-level attention aggre-gation, in Proceedings of the IEEE/CVF Conference on ComputerVision and Pattern Recognition, 2022, pp. 13 648–13 657.
  * M. Oquab, T. Darcet, T. Moutakanni, H. V o, M. Szafraniec, V. Khali-dov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby et al., Dinov2:Learning robust visual features without supervision, arXiv preprintarXiv:2304.07193, 2023.
  * N. Keetha, A. Mishra, J. Karhade, K. M. Jatavallabhula, S. Scherer, M. Krishna, and S. Garg, Anyloc: Towards universal visual placerecognition, IEEE Robotics and Automation Letters, 2023.
  * N. Piasco, D. Sidibe, V. Gouet-Brunet, and C. Demonceaux, Learningscene geometry for visual localization in challenging conditions, in2019 International Conference on Robotics and Automation (ICRA).IEEE, 2019, pp. 9094–9100.
  * G. Peng, Y. Yue, J. Zhang, Z. Wu, X. Tang, and D. Wang, Semanticreinforced attention learning for visual place recognition, in 2021IEEE International Conference on Robotics and Automation (ICRA),2021, pp. 13 415–13 422.
  * A. Oertel, T. Cieslewski, and D. Scaramuzza, Augmenting visualplace recognition with structural cues, IEEE Robotics and AutomationLetters, vol. 5, no. 4, pp. 5534–5541, 2020.
  * J. Komorowski, M. Wysoczanska, and T. Trzcinski, Minkloc++:lidar and monocular image fusion for place recognition, in 2021International Joint Conference on Neural Networks (IJCNN). IEEE,2021, pp. 1–8.
  * A. J. Lee and A. Kim, Eventvlad: Visual place recognition with recon-structed edges from event cameras, in 2021 IEEE/RSJ InternationalConference on Intelligent Robots and Systems (IROS), 2021, pp. 2247–2252.

<a id="range_based_approach"></a>
### Range Sensor-Related Approaches 
  * R. Q. Charles, H. Su, M. Kaichun, and L. J. Guibas, Pointnet:Deep learning on point sets for 3d classification and segmentation, in2017 IEEE Conference on Computer Vision and Pattern Recognition(CVPR), 2017, pp. 77–85.
  * C. Choy, J. Gwak, and S. Savarese, 4d spatio-temporal convnets:Minkowski convolutional neural networks, in Proceedings of the IEEEConference on Computer Vision and Pattern Recognition, 2019, pp.3075–3084.
  * G. Kim and A. Kim, Scan context: Egocentric spatial descriptorfor place recognition within 3d point cloud map, in 2018 IEEE/RSJInternational Conference on Intelligent Robots and Systems (IROS),2018, pp. 4802–4809.
  * G. Kim, S. Choi, and A. Kim, Scan context++: Structural place recog-nition robust to rotation and lateral variations in urban environments,IEEE Transactions on Robotics, vol. 38, no. 3, pp. 1856–1874, 2022.
  * Y. Wang, Z. Sun, C.-Z. Xu, S. E. Sarma, J. Yang, and H. Kong,Lidar iris for loop-closure detection, in 2020 IEEE/RSJ InternationalConference on Intelligent Robots and Systems (IROS). IEEE, 2020,pp. 5769–5775.
  * X. Xu, S. Lu, J. Wu, H. Lu, Q. Zhu, Y. Liao, R. Xiong, and Y. Wang,Ring++: Roto-translation invariant gram for global localization on a17sparse scan map, IEEE Transactions on Robotics, vol. 39, no. 6, pp.4616–4635, 2023.
  * C. Yuan, J. Lin, Z. Liu, H. Wei, X. Hong, and F. Zhang, Btc: Abinary and triangle combined descriptor for 3-d place recognition,IEEE Transactions on Robotics, vol. 40, pp. 1580–1599, 2024.
  * M. Jiang, Y. Wu, T. Zhao, Z. Zhao, and C. Lu, Pointsift: A sift-like network module for 3d point cloud semantic segmentation, arXivpreprint arXiv:1807.00652, 2018.
  * M. A. Uy and G. H. Lee, Pointnetvlad: Deep point cloud basedretrieval for large-scale place recognition, in 2018 IEEE/CVF Con-ference on Computer Vision and Pattern Recognition, 2018, pp. 4470–4479.
  * R. Arandjelovic, P. Gronat, A. Torii, T. Pajdla, and J. Sivic, Netvlad:Cnn architecture for weakly supervised place recognition, in 2016IEEE Conference on Computer Vision and Pattern Recognition(CVPR), 2016, pp. 5297–5307.
  * Z. Liu, S. Zhou, C. Suo, P. Yin, W. Chen, H. Wang, H. Li, and Y. Liu,Lpd-net: 3d point cloud learning for large-scale place recognition andenvironment analysis, in 2019 IEEE/CVF International Conference onComputer Vision (ICCV), 2019, pp. 2831–2840.
  * Y. Xia, Y. Xu, S. Li, R. Wang, J. Du, D. Cremers, and U. Stilla, Soe-net: A self-attention and orientation encoding network for point cloudbased place recognition, in Proceedings of the IEEE/CVF Conferenceon computer vision and pattern recognition, 2021, pp. 11 348–11 357.
  * Z. Fan, Z. Song, W. Zhang, H. Liu, J. He, and X. Du, Rpr-net: A pointcloud-based rotation-aware large scale place recognition network, inEuropean Conference on Computer Vision. Springer, 2022, pp. 709–725.
  * Y. You, Y. Lou, R. Shi, Q. Liu, Y.-W. Tai, L. Ma, W. Wang, and C. Lu,Prin/sprin: On extracting point-wise rotation invariant features, IEEETransactions on Pattern Analysis and Machine Intelligence, vol. 44,no. 12, pp. 9489–9502, 2021.
  * J. Komorowski, Minkloc3d: Point cloud based large-scale place recog-nition, in 2021 IEEE Winter Conference on Applications of ComputerVision (WACV), 2021, pp. 1789–1798.
  * K. Vidanapathirana, M. Ramezani, P. Moghadam, S. Sridharan, andC. Fookes, Logg3d-net: Locally guided global descriptor learning for3d place recognition, in 2022 International Conference on Roboticsand Automation (ICRA), 2022, pp. 2215–2221.
  * P. Yin, F. Wang, A. Egorov, J. Hou, Z. Jia, and J. Han, Fast sequence-matching enhanced viewpoint-invariant 3-d place recognition, IEEETransactions on Industrial Electronics, vol. 69, no. 2, pp. 2127–2135,2022.
  * L. Luo, S. Zheng, Y. Li, Y. Fan, B. Yu, S.-Y. Cao, J. Li, and H.-L. Shen,Bevplace: Learning lidar-based place recognition using bird’s eye viewimages, in Proceedings of the IEEE/CVF International Conference onComputer Vision, 2023, pp. 8700–8709.
  * K. ˙Zywanowski, A. Banaszczyk, M. R. Nowicki, and J. Komorowski,Minkloc3d-si: 3d lidar place recognition with sparse convolutions,spherical coordinates, and intensity, IEEE Robotics and AutomationLetters, vol. 7, no. 2, pp. 1079–1086, 2022.
  * X. Chen, T. L ¨abe, A. Milioto, T. R ¨ohling, O. Vysotska, A. Haag,J. Behley, and C. Stachniss, Overlapnet: Loop closing for lidar-basedSLAM, CoRR, vol. abs/2105.11344, 2021.
  * J. Ma, J. Zhang, J. Xu, R. Ai, W. Gu, and X. Chen, Overlaptrans-former: An efficient and yaw-angle-invariant transformer network forlidar-based place recognition, IEEE Robotics and Automation Letters,vol. 7, no. 3, pp. 6958–6965, 2022.
  * L. Li, X. Kong, X. Zhao, T. Huang, W. Li, F. Wen, H. Zhang, andY. Liu, Rinet: Efficient 3d lidar-based place recognition using rotationinvariant neural network, IEEE Robotics and Automation Letters,vol. 7, no. 2, pp. 4321–4328, 2022.
  * P. Yin, L. Xu, J. Zhang, H. Choset, and S. Scherer, i3dloc: Image-to-range cross-domain localization robust to inconsistent environmentalconditions, in Proceedings of Robotics: Science and Systems (RSS’21). Robotics: Science and Systems 2021, 2021.
  * S. Zhao, P. Yin, G. Yi, and S. Scherer, Spherevlad++: Attention-basedand signal-enhanced viewpoint invariant descriptor, 2022.
  * X. Xu, H. Yin, Z. Chen, Y. Li, Y. Wang, and R. Xiong, Disco: Differ-entiable scan context with orientation, IEEE Robotics and AutomationLetters, vol. 6, no. 2, pp. 2791–2798, 2021.
  * S. Saftescu, M. Gadd, D. De Martini, D. Barnes, and P. Newman,Kidnapped radar: Topological radar localisation using rotationally-invariant metric learning, in 2020 IEEE International Conference onRobotics and Automation (ICRA), 2020, pp. 4358–4364.
  * K. Cait, B. Wang, and C. X. Lu, Autoplace: Robust place recognitionwith single-chip automotive radar, in 2022 International Conferenceon Robotics and Automation (ICRA), 2022, pp. 2222–2228.
  * C. Meng, Y. Duan, C. He, D. Wang, X. Fan, and Y. Zhang, mmplace:Robust place recognition with intermediate frequency signal of low-cost single-chip millimeter wave radar, IEEE Robotics and AutomationLetters, 2024.
  * N. Hughes, Y. Chang, and L. Carlone, Hydra: A real-time spatialperception system for 3d scene graph construction and optimization,arXiv preprint arXiv:2201.13360, 2022.
  * M. Gadd, D. De Martini, and P. Newman, Look around you:Sequence-based radar place recognition with learned rotational invari-ance, in 2020 IEEE/ION Position, Location and Navigation Sympo-sium (PLANS), 2020, pp. 270–276.
  * T. Y. Tang, D. D. Martini, S. Wu, and P. Newman, Self-supervisedlearning for using overhead imagery as maps in outdoor range sensorlocalization, The International Journal of Robotics Research, vol. 40,no. 12-14, pp. 1488–1509, 2021, pMID: 34992328.
  * M. Gadd, D. De Martini, and P. Newman, Contrastive learning forunsupervised radar place recognition, in 2021 20th InternationalConference on Advanced Robotics (ICAR), 2021, pp. 344–349.

## High-Level Representation

<a id="graph"></a>
### Graph: 
  * N. Hughes, Y. Chang, and L. Carlone, Hydra: A real-time spatialperception system for 3d scene graph construction and optimization,arXiv preprint arXiv:2201.13360, 2022.
  * E. Stumm, C. Mei, S. Lacroix, J. Nieto, M. Hutter, and R. Siegwart,Robust visual place recognition with graph kernels, in Proceedingsof the IEEE Conference on Computer Vision and Pattern Recognition,2016, pp. 4535–4544.
  * N. Kim, O. Kwon, H. Yoo, Y. Choi, J. Park, and S. Oh, Topologicalsemantic graph memory for image-goal navigation, in Conference onRobot Learning. PMLR, 2023, pp. 393–402.
  * X. Kong, X. Yang, G. Zhai, X. Zhao, X. Zeng, M. Wang, Y. Liu, W. Li,and F. Wen, Semantic graph based place recognition for 3d pointclouds, in 2020 IEEE/RSJ International Conference on IntelligentRobots and Systems (IROS). IEEE, 2020, pp. 8216–8223.
  * K. Vidanapathirana, P. Moghadam, B. Harwood, M. Zhao, S. Sridharan,and C. Fookes, Locus: Lidar-based place recognition using spatiotem-poral higher-order pooling, in 2021 IEEE International Conference onRobotics and Automation (ICRA), 2021, pp. 5075–5081.
  * N. Hughes, Y. Chang, and L. Carlone, Hydra: A real-time spatial perception system for 3d scene graph construction and optimization, arXiv preprint arXiv:2201.13360, 2022
  
<a id="embedding"></a>
### Embeddings: 
  * O. Kwon, J. Park, and S. Oh, Renderable neural radiance map forvisual navigation, in Proceedings of the IEEE/CVF Conference onComputer Vision and Pattern Recognition, 2023, pp. 9099–9108.
  * A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal,G. Sastry, A. Askell, P. Mishkin, J. Clark et al., Learning transferablevisual models from natural language supervision, in Internationalconference on machine learning. PMLR, 2021, pp. 8748–8763.
  * C. Kassab, M. Mattamala, L. Zhang, and M. Fallon, Language-extended indoor slam (lexis): A versatile system for real-time visualscene understanding, arXiv preprint arXiv:2309.15065, 2023.
  * J. Chen, D. Barath, I. Armeni, M. Pollefeys, and H. Blum,  where ami? scene retrieval with language, arXiv preprint arXiv:2404.14565, 2024.
  * Z. Hong, Y. Petillot, D. Lane, Y. Miao, and S. Wang, Textplace: Visualplace recognition and topological localization through reading scenetexts, in Proceedings of the IEEE/CVF International Conference onComputer Vision, 2019, pp. 2861–2870.
  * P. Yin, L. Xu, J. Zhang, H. Choset, and S. Scherer, i3dloc: Image-to-range cross-domain localization robust to inconsistent environmentalconditions, in Proceedings of Robotics: Science and Systems (RSS’21). Robotics: Science and Systems 2021, 2021.
  * S. Garg and M. Milford, Seqnet: Learning descriptors for sequence-based hierarchical place recognition, IEEE Robotics and AutomationLetters, vol. 6, no. 3, pp. 4305–4312, 2021.

<a id="recognize_challenge"></a>
# Recognizing the Right Place Aginst Challenges

<a id="appearance_change"></a>
## A. Appearance Change 
### A.1 Place Modeling
  * G. Peng, Y. Yue, J. Zhang, Z. Wu, X. Tang, and D. Wang, Semanticreinforced attention learning for visual place recognition, in 2021IEEE International Conference on Robotics and Automation (ICRA),2021, pp. 13 415–13 422.
  * N. Merrill and G. Huang, Calc2.0: Combining appearance, semanticand geometric information for robust and efficient visual loop closure,in2019 IEEE/RSJ International Conference on Intelligent Robots andSystems (IROS), 2019, pp. 4554–4561.
  * S. Hausler, S. Garg, M. Xu, M. Milford, and T. Fischer, Patch-netvlad: Multi-scale fusion of locally-global descriptors for placerecognition, in 2021 IEEE/CVF Conference on Computer Vision andPattern Recognition (CVPR), 2021, pp. 14 136–14 147.
  * P. Yin, L. Xu, X. Li, C. Yin, Y. Li, R. A. Srivatsan, L. Li, J. Ji, andY. He, A multi-domain feature learning method for visual place recog-nition, in 2019 International Conference on Robotics and Automation(ICRA), 2019, pp. 319–324.
  * P. Yin, I. Cisneros, S. Zhao, J. Zhang, H. Choset, and S. Scherer,isimloc: Visual global localization for previously unseen environmentswith simulated images, IEEE Transactions on Robotics, 2023.
  * P. Yin, L. Xu, J. Zhang, H. Choset, and S. Scherer, i3dloc: Image-to-range cross-domain localization robust to inconsistent environmentalconditions, in Proceedings of Robotics: Science and Systems (RSS’21). Robotics: Science and Systems 2021, 2021.
### A.2 Place Matching with Sequences
  * M. J. Milford and G. F. Wyeth, Seqslam: Visual route-based navigationfor sunny summer days and stormy winter nights, in 2012 IEEEInternational Conference on Robotics and Automation, 2012, pp. 1643–1649.
  * F. Lu, B. Chen, X.-D. Zhou, and D. Song, Sta-vpr: Spatio-temporalalignment for visual place recognition, IEEE Robotics and AutomationLetters, vol. 6, no. 3, pp. 4297–4304, 2021.
  * S. Garg and M. Milford, Seqnet: Learning descriptors for sequence-based hierarchical place recognition, IEEE Robotics and AutomationLetters, vol. 6, no. 3, pp. 4305–4312, 2021.
  * S. M. Siam and H. Zhang, Fast-seqslam: A fast appearance basedplace recognition algorithm, in 2017 IEEE International Conferenceon Robotics and Automation (ICRA), 2017, pp. 5702–5708.
  * P. Yin, F. Wang, A. Egorov, J. Hou, J. Zhang, and H. Choset, Se-qspherevlad: Sequence matching enhanced orientation-invariant placerecognition, in 2020 IEEE/RSJ International Conference on IntelligentRobots and Systems (IROS), 2020, pp. 5024–5029.
  * L. Bampis, A. Amanatiadis, and A. Gasteratos, Fast loop-closuredetection using visual-word-vectors from image sequences, The In-ternational Journal of Robotics Research, vol. 37, no. 1, pp. 62–82,2018.

<a id="viewpoint_diference"></a>
## B. Viewpoint Difference 
  * P. Yin, I. Cisneros, S. Zhao, J. Zhang, H. Choset, and S. Scherer,isimloc: Visual global localization for previously unseen environmentswith simulated images, IEEE Transactions on Robotics, 2023.
  * J. Ma, J. Zhang, J. Xu, R. Ai, W. Gu, and X. Chen, Overlaptrans-former: An efficient and yaw-angle-invariant transformer network forlidar-based place recognition, IEEE Robotics and Automation Letters,vol. 7, no. 3, pp. 6958–6965, 2022.
  * Z. Fan, Z. Song, W. Zhang, H. Liu, J. He, and X. Du, Rpr-net: A pointcloud-based rotation-aware large scale place recognition network, inEuropean Conference on Computer Vision. Springer, 2022, pp. 709–725.
  * Y. You, Y. Lou, R. Shi, Q. Liu, Y.-W. Tai, L. Ma, W. Wang, and C. Lu,Prin/sprin: On extracting point-wise rotation invariant features, IEEETransactions on Pattern Analysis and Machine Intelligence, vol. 44,no. 12, pp. 9489–9502, 2022.
  * A. Ali-Bey, B. Chaib-Draa, and P. Giguere, Mixvpr: Feature mixingfor visual place recognition, in Proceedings of the IEEE/CVF WinterConference on Applications of Computer Vision, 2023, pp. 2998–3007.
  * S. Hausler, S. Garg, M. Xu, M. Milford, and T. Fischer, Patch-netvlad: Multi-scale fusion of locally-global descriptors for placerecognition, in 2021 IEEE/CVF Conference on Computer Vision andPattern Recognition (CVPR), 2021, pp. 14 136–14 147.
  * P. Yin, S. Zhao, H. Lai, R. Ge, J. Zhang, H. Choset, and S. Scherer,Automerge: A framework for map assembling and smoothing in city-scale environments, IEEE Transactions on Robotics, 2023.18
  * J. Knights, P. Moghadam, M. Ramezani, S. Sridharan, and C. Fookes,Incloud: Incremental learning for point cloud place recognition, in2022 IEEE/RSJ International Conference on Intelligent Robots andSystems (IROS). IEEE, 2022, pp. 8559–8566.
  * G. Kim and A. Kim, Scan context: Egocentric spatial descriptorfor place recognition within 3d point cloud map, in 2018 IEEE/RSJInternational Conference on Intelligent Robots and Systems (IROS),2018, pp. 4802–4809.
  * P. Yin, L. Xu, J. Zhang, H. Choset, and S. Scherer, i3dloc: Image-to-range cross-domain localization robust to inconsistent environmentalconditions, in Proceedings of Robotics: Science and Systems (RSS’21). Robotics: Science and Systems 2021, 2021.
  * P. Yin, L. Xu, J. Zhang, and H. Choset, Fusionvlad: A multi-viewdeep fusion networks for viewpoint-free 3d place recognition, IEEERobotics and Automation Letters, vol. 6, no. 2, pp. 2304–2310, 2021.

<a id="generalization_ability"></a>
## C. Generalization Ability 
  * B. Neyshabur, S. Bhojanapalli, D. McAllester, and N. Srebro, Explor-ing generalization in deep learning, Advances in neural informationprocessing systems, vol. 30, 2017.
  * K. Simonyan and A. Zisserman, Very deep convolutional networksfor large-scale image recognition, in 3rd International Conference onLearning Representations, ICLR 2015, San Diego, CA, USA, May 7-9,2015, Conference Track Proceedings, Y. Bengio and Y. LeCun, Eds.,2015.
  * R. Arandjelovic, P. Gronat, A. Torii, T. Pajdla, and J. Sivic, Netvlad:Cnn architecture for weakly supervised place recognition, in 2016IEEE Conference on Computer Vision and Pattern Recognition(CVPR), 2016, pp. 5297–5307.
  * S. Zhao, P. Yin, G. Yi, and S. Scherer, Spherevlad++: Attention-basedand signal-enhanced viewpoint invariant descriptor, 2022.
  * N. Keetha, A. Mishra, J. Karhade, K. M. Jatavallabhula, S. Scherer,M. Krishna, and S. Garg, Anyloc: Towards universal visual placerecognition, IEEE Robotics and Automation Letters, 2023.
  * P. Yin, L. Xu, Z. Feng, A. Egorov, and B. Li, Pse-match: A viewpoint-free place recognition method with parallel semantic embedding, IEEETransactions on Intelligent Transportation Systems, pp. 1–12, 2021.
  * V. Paolicelli, A. Tavera, C. Masone, G. Berton, and B. Caputo,Learning semantics for visual place recognition through multi-scaleattention, in Image Analysis and Processing – ICIAP 2022, S. Sclaroff,C. Distante, M. Leo, G. M. Farinella, and F. Tombari, Eds. Cham:Springer International Publishing, 2022, pp. 454–466.
  * H. Lai, P. Yin, and S. Scherer, Adafusion: Visual-lidar fusion withadaptive weights for place recognition, 2021.
  * J. Komorowski, M. Wysoczanska, and T. Trzcinski, Minkloc++:lidar and monocular image fusion for place recognition, in 2021International Joint Conference on Neural Networks (IJCNN). IEEE,2021, pp. 1–8.
  * M. A. Uy and G. H. Lee, Pointnetvlad: Deep point cloud basedretrieval for large-scale place recognition, in 2018 IEEE/CVF Con-ference on Computer Vision and Pattern Recognition, 2018, pp. 4470–4479.
  * P. Yin, F. Wang, A. Egorov, J. Hou, Z. Jia, and J. Han, Fast sequence-matching enhanced viewpoint-invariant 3-d place recognition, IEEETransactions on Industrial Electronics, vol. 69, no. 2, pp. 2127–2135,2022.
  * T. Barros, L. Garrote, R. Pereira, C. Premebida, and U. J. Nunes,Attdlnet: Attention-based dl network for 3d lidar place recognition,2021.
  * L. Li, X. Kong, X. Zhao, T. Huang, W. Li, F. Wen, H. Zhang, andY. Liu, Rinet: Efficient 3d lidar-based place recognition using rotationinvariant neural network, IEEE Robotics and Automation Letters,vol. 7, no. 2, pp. 4321–4328, 2022.
  * D. Gao, C. Wang, and S. Scherer, Airloop: Lifelong loop closure de-tection, in 2022 International Conference on Robotics and Automation(ICRA). IEEE, 2022, pp. 10 664–10 671.
  * J. Knights, P. Moghadam, M. Ramezani, S. Sridharan, and C. Fookes,Incloud: Incremental learning for point cloud place recognition, in2022 IEEE/RSJ International Conference on Intelligent Robots andSystems (IROS). IEEE, 2022, pp. 8559–8566.
  * A.-D. Doan, Y. Latif, T.-J. Chin, and I. Reid, Hm4: Hidden markovmodel with memory management for visual place recognition, IEEERobotics and Automation Letters, vol. 6, no. 1, pp. 167–174, 2021.
  * P. Yin, A. Abuduweili, S. Zhao, L. Xu, C. Liu, and S. Scherer,Bioslam: A bioinspired lifelong memory system for general placerecognition, IEEE Transactions on Robotics, 2023.

<a id="efficiency"></a>
## D. Efficiency 
  * D. Galvez-Lopez and J. D. Tardos, Bags of binary words for fastplace recognition in image sequences, IEEE Transactions on Robotics,vol. 28, no. 5, pp. 1188–1197, 2012.
  * G. Kim and A. Kim, Scan context: Egocentric spatial descriptorfor place recognition within 3d point cloud map, in 2018 IEEE/RSJInternational Conference on Intelligent Robots and Systems (IROS),2018, pp. 4802–4809.
  * G. Kim, S. Choi, and A. Kim, Scan context++: Structural place recog-nition robust to rotation and lateral variations in urban environments,IEEE Transactions on Robotics, vol. 38, no. 3, pp. 1856–1874, 2022.
  * H. Wang, C. Wang, and L. Xie, Intensity scan context: Codingintensity and geometry relations for loop closure detection, in 2020IEEE International Conference on Robotics and Automation (ICRA).IEEE, 2020, pp. 2095–2101.
  * M. Sandler, A. Howard, M. Zhu, A. Zhmoginov, and L.-C. Chen, Mo-bilenetv2: Inverted residuals and linear bottlenecks, in Proceedings ofthe IEEE conference on computer vision and pattern recognition, 2018,pp. 4510–4520.
  * B. Ferrarini, M. J. Milford, K. D. McDonald-Maier, and S. Ehsan,Binary neural networks for memory-efficient and effective visual placerecognition in changing environments, IEEE Transactions on Robotics,vol. 38, no. 4, pp. 2617–2631, 2022.
  * O. Grainge, M. Milford, I. Bodala, S. D. Ramchurn, and S. Ehsan,Design space exploration of low-bit quantized neural networks forvisual place recognition, arXiv preprint arXiv:2312.09028, 2023.
  * W. Maass, Networks of spiking neurons: the third generation of neuralnetwork models, Neural networks, vol. 10, no. 9, pp. 1659–1671,1997.
  * A. D. Hines, P. G. Stratton, M. Milford, and T. Fischer, Vprtempo:A fast temporally encoded spiking neural network for visual placerecognition, arXiv preprint arXiv:2309.10225, 2023.
  * S. Hussaini, M. Milford, and T. Fischer, Applications of spik-ing neural networks in visual place recognition, arXiv preprintarXiv:2311.13186, 2023.
  * M. J. Milford and G. F. Wyeth, Seqslam: Visual route-based navigationfor sunny summer days and stormy winter nights, in 2012 IEEEInternational Conference on Robotics and Automation, 2012, pp. 1643–1649.
  * Y. Liu and H. Zhang, Towards improving the efficiency of sequence-based slam, in 2013 IEEE International Conference on Mechatronicsand Automation, 2013, pp. 1261–1266.
  * S. M. Siam and H. Zhang, Fast-seqslam: A fast appearance basedplace recognition algorithm, in 2017 IEEE International Conferenceon Robotics and Automation (ICRA), 2017, pp. 5702–5708.
  * P. Hansen and B. Browning, Visual place recognition using hmmsequence matchingv, in 2014 IEEE/RSJ International Conference onIntelligent Robots and Systems, 2014, pp. 4549–4555.
  * P. Yin, R. A. Srivatsan, Y. Chen, X. Li, H. Zhang, L. Xu, L. Li, Z. Jia,J. Ji, and Y. He, Mrs-vpr: a multi-resolution sampling based globalvisual place recognition method, in 2019 International Conference onRobotics and Automation (ICRA), 2019, pp. 7137–7142.
  * P. Yin, F. Wang, A. Egorov, J. Hou, J. Zhang, and H. Choset, Se-qspherevlad: Sequence matching enhanced orientation-invariant placerecognition, in 2020 IEEE/RSJ International Conference on IntelligentRobots and Systems (IROS), 2020, pp. 5024–5029.

<a id="uncertainty_estimation"></a>
## E. Uncertainty Estimation 
  * L. Carlone, G. C. Calafiore, C. Tommolillo, and F. Dellaert, Planarpose graph optimization: Duality, optimal solutions, and verification,IEEE Transactions on Robotics, vol. 32, no. 3, pp. 545–565, 2016.
  * P. Yin, S. Zhao, H. Lai, R. Ge, J. Zhang, H. Choset, and S. Scherer,Automerge: A framework for map assembling and smoothing in city-scale environments, IEEE Transactions on Robotics, 2023.18
  * X. Hu, L. Zheng, J. Wu, R. Geng, Y. Yu, H. Wei, X. Tang, L. Wang,J. Jiao, and M. Liu, Paloc: Advancing slam benchmarking with prior-assisted 6-dof trajectory generation and uncertainty estimation, arXivpreprint arXiv:2401.17826, 2024.
  * Y. Gal and Z. Ghahramani, Dropout as a bayesian approximation:Representing model uncertainty in deep learning, in InternationalConference on Machine Learning, 2016, pp. 1050–1059.
  * B. Lakshminarayanan, A. Pritzel, and C. Blundell, Simple and scalablepredictive uncertainty estimation using deep ensembles, Advances inneural information processing systems, vol. 30, 2017.
  * P. Yun and M. Liu, Laplace approximation based epistemic uncertaintyestimation in 3d object detection, in Conference on Robot Learning.PMLR, 2023, pp. 1125–1135.
  * A. Kendall and Y. Gal, What uncertainties do we need in bayesiandeep learning for computer vision? Advances in neural informationprocessing systems, vol. 30, 2017.
  * K. Cai, C. X. Lu, and X. Huang, Stun: Self-teaching uncertaintyestimation for place recognition, in 2022 IEEE/RSJ InternationalConference on Intelligent Robots and Systems (IROS). IEEE, 2022,pp. 6614–6621.
  * M. Sensoy, L. Kaplan, and M. Kandemir, Evidential deep learningto quantify classification uncertainty, Advances in neural informationprocessing systems, vol. 31, 2018.
  * K. Mason, J. Knights, M. Ramezani, P. Moghadam, and D. Miller,Uncertainty-aware lidar place recognition in novel environments, in2023 IEEE/RSJ International Conference on Intelligent Robots andSystems (IROS). IEEE, 2023, pp. 3366–3373.
  * Y. Shi and A. K. Jain, Probabilistic face embeddings, in Proceedingsof the IEEE/CVF International Conference on Computer Vision, 2019,pp. 6902–6911.

<a id="application"></a>
# Application & Trends
<a id="navigaiton"></a>
## A. Long-Term & Large-Scale Navigation 
  * L. Chen, P. Wu, K. Chitta, B. Jaeger, A. Geiger, and H. Li, End-to-end autonomous driving: Challenges and frontiers, arXiv preprintarXiv:2306.16927, 2023.19
  * M. Tranzatto, T. Miki, M. Dharmadhikari, L. Bernreiter, M. Kulkarni,F. Mascarich, O. Andersson, S. Khattak, M. Hutter, R. Siegwart et al.,Cerberus in the darpa subterranean challenge, Science Robotics,vol. 7, no. 66, p. eabp9742, 2022.
  * C. Campos, R. Elvira, J. J. G. Rodrıguez, J. M. Montiel, and J. D.Tardos, Orb-slam3: An accurate open-source library for visual, visual–inertial, and multimap slam, IEEE Transactions on Robotics, vol. 37,no. 6, pp. 1874–1890, 2021.
  * T. Qin, P. Li, and S. Shen, Vins-mono: A robust and versatile monoc-ular visual-inertial state estimator, IEEE Transactions on Robotics,vol. 34, no. 4, pp. 1004–1020, 2018.
  * D. Galvez-Lopez and J. D. Tardos, Bags of binary words for fastplace recognition in image sequences, IEEE Transactions on Robotics,vol. 28, no. 5, pp. 1188–1197, 2012.
  * T. Shan, B. Englot, C. Ratti, and D. Rus, Lvi-sam: Tightly-coupledlidar-visual-inertial odometry via smoothing and mapping, in 2021IEEE international conference on robotics and automation (ICRA).IEEE, 2021, pp. 5692–5698.
  * D. Adolfsson, M. Karlsson, V. Kubelka, M. Magnusson, and H. An-dreasson, Tbv radar slam–trust but verify loop candidates, IEEERobotics and Automation Letters, 2023.
  * W. Chen, L. Zhu, Y. Guan, C. R. Kube, and H. Zhang, Submap-basedpose-graph visual slam: A robust visual exploration and localizationsystem, in 2018 IEEE/RSJ International Conference on IntelligentRobots and Systems (IROS). IEEE, 2018, pp. 6851–6856.
  * M. Kuse and S. Shen, Learning whole-image descriptors for real-timeloop detection and kidnap recovery under large viewpoint difference,Robotics and Autonomous Systems, vol. 143, p. 103813, 2021.
  * M. A. Uy and G. H. Lee, Pointnetvlad: Deep point cloud basedretrieval for large-scale place recognition, in 2018 IEEE/CVF Con-ference on Computer Vision and Pattern Recognition, 2018, pp. 4470–4479.
  * D. DeTone, T. Malisiewicz, and A. Rabinovich, Superpoint: Self-supervised interest point detection and description, in Proceedingsof the IEEE conference on computer vision and pattern recognitionworkshops, 2018, pp. 224–236.
  * P.-E. Sarlin, C. Cadena, R. Siegwart, and M. Dymczyk, From coarse tofine: Robust hierarchical localization at large scale, in 2019 IEEE/CVFConference on Computer Vision and Pattern Recognition (CVPR),2019, pp. 12 708–12 717.
  * P. Yin, L. Xu, J. Zhang, H. Choset, and S. Scherer, i3dloc: Image-to-range cross-domain localization robust to inconsistent environmentalconditions, in Proceedings of Robotics: Science and Systems (RSS’21). Robotics: Science and Systems 2021, 2021.
  * L. Liu and H. Li, Lending orientation to neural networks for cross-view geo-localization, in 2019 IEEE/CVF Conference on ComputerVision and Pattern Recognition (CVPR), 2019, pp. 5617–5626.
  * F. Gao, L. Wang, B. Zhou, X. Zhou, J. Pan, and S. Shen, Teach-repeat-replan: A complete and robust system for aggressive flight incomplex environments, IEEE Transactions on Robotics, vol. 36, no. 5,pp. 1526–1545, 2020.
  * M. Mattamala, M. Ramezani, M. Camurri, and M. Fallon, Learningcamera performance models for active multi-camera visual teach andrepeat, in 2021 IEEE International Conference on Robotics andAutomation (ICRA). IEEE, 2021, pp. 14 346–14 352.
  * Y. Chen and T. D. Barfoot, Self-supervised feature learning forlong-term metric visual localization, IEEE Robotics and AutomationLetters, vol. 8, no. 2, pp. 472–479, 2022.
  * L. Suomela, J. Kalliola, A. Dag, H. Edelman, and J.-K. K ¨am¨ar¨ainen,Placenav: Topological navigation through place recognition, arXivpreprint arXiv:2309.17260, 2023.
  * N. Hughes, Y. Chang, and L. Carlone, Hydra: A real-time spatialperception system for 3d scene graph construction and optimization,arXiv preprint arXiv:2201.13360, 2022.
  * O. Michel, A. Bhattad, E. VanderBilt, R. Krishna, A. Kembhavi, andT. Gupta, Object 3dit: Language-guided 3d-aware image editing,Advances in Neural Information Processing Systems, vol. 36, 2024.

<a id="vtrn"></a>
## B. Visual Terrain Relative Navigation 
  * A. T. Fragoso, C. T. Lee, A. S. McCoy, and S.-J. Chung, A seasonallyinvariant deep transform for visual terrain-relative navigation, ScienceRobotics, vol. 6, no. 55, p. eabf3320, 2021.
  * P. Yin, I. Cisneros, S. Zhao, J. Zhang, H. Choset, and S. Scherer,isimloc: Visual global localization for previously unseen environmentswith simulated images, IEEE Transactions on Robotics, 2023.
  * M. Bianchi and T. D. Barfoot, Uav localization using autoencodedsatellite images, IEEE Robotics and Automation Letters, vol. 6, no. 2,pp. 1761–1768, 2021.
  * B. Patel, T. D. Barfoot, and A. P. Schoellig, Visual localization withgoogle earth images for robust global pose estimation of uavs, in 2020IEEE International Conference on Robotics and Automation (ICRA).IEEE, 2020, pp. 6491–6497.
  * L. Liu and H. Li, Lending orientation to neural networks for cross-view geo-localization, in 2019 IEEE/CVF Conference on ComputerVision and Pattern Recognition (CVPR), 2019, pp. 5617–5626.
  * P.-E. Sarlin, E. Trulls, M. Pollefeys, J. Hosang, and S. Lynen, Snap:Self-supervised neural maps for visual positioning and semantic under-standing, Advances in Neural Information Processing Systems, vol. 36,2024.
  * T. Y. Tang, D. De Martini, and P. Newman, Get to the point: Learninglidar place recognition and metric localisation using overhead imagery,Proceedings of Robotics: Science and Systems, 2021, 2021.
  * Y. Shi, F. Wu, A. Perincherry, A. V ora, and H. Li, Boosting 3-dofground-to-satellite camera localization accuracy via geometry-guidedcross-view transformer, in Proceedings of the IEEE/CVF InternationalConference on Computer Vision, 2023, pp. 21 516–21 526.
  * A. Witze et al., Nasa has launched the most ambitious mars roverever built: Here’s what happens next, Nature, vol. 584, no. 7819, pp.15–16, 2020.
  * L. Ding, R. Zhou, Y. Yuan, H. Yang, J. Li, T. Yu, C. Liu, J. Wang,S. Li, H. Gao, Z. Deng, N. Li, Z. Wang, Z. Gong, G. Liu, J. Xie,S. Wang, Z. Rong, D. Deng, X. Wang, S. Han, W. Wan, L. Richter,L. Huang, S. Gou, Z. Liu, H. Yu, Y. Jia, B. Chen, Z. Dang, K. Zhang,L. Li, X. He, S. Liu, and K. Di, A 2-year locomotive exploration andscientific investigation of the lunar farside by the yutu-2 rover, ScienceRobotics, vol. 7, no. 62, p. eabj6660, 2022.
  * I. D. Miller, F. Cladera, T. Smith, C. J. Taylor, and V. Kumar,Stronger together: Air-ground robotic collaboration using semantics,IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 9643–9650,2022.

<a id="multi-agent-slam"></a>
## C. Multi-Agent Localization and Mapping 
  * J. Yan, X. Lin, Z. Ren, S. Zhao, J. Yu, C. Cao, P. Yin, J. Zhang,and S. Scherer, Mui-tare: Multi-agent cooperative exploration withunknown initial position, arXiv preprint arXiv:2209.10775, 2022.
  * Y. Tian, Y. Chang, F. H. Arias, C. Nieto-Granda, J. P. How, andL. Carlone, Kimera-multi: Robust, distributed, dense metric-semanticslam for multi-robot systems, IEEE Transactions on Robotics, pp. 1–17, 2022.
  * D. Van Opdenbosch and E. Steinbach, Collaborative visual slam usingcompressed feature exchange, IEEE Robotics and Automation Letters,vol. 4, no. 1, pp. 57–64, 2019.
  * T. Sasaki, K. Otsu, R. Thakker, S. Haesaert, and A.-a. Agha-mohammadi, Where to map? iterative rover-copter path planning formars exploration, IEEE Robotics and Automation Letters, vol. 5, no. 2,pp. 2123–2130, 2020.
  * K. Ebadi, Y. Chang, M. Palieri, A. Stephens, A. Hatteland, E. Heiden,A. Thakur, N. Funabiki, B. Morrell, S. Wood, L. Carlone, and A.-a. Agha-mohammadi, Lamp: Large-scale autonomous mapping andpositioning for exploration of perceptually-degraded subterranean en-vironments, in 2020 IEEE International Conference on Robotics andAutomation (ICRA), 2020, pp. 80–86.
  * Y. Chang, N. Hughes, A. Ray, and L. Carlone, Hydra-multi: Collabo-rative online construction of 3d scene graphs with multi-robot teams,arXiv preprint arXiv:2304.13487, 2023.
  * M. Labbe and F. Michaud, Rtab-map as an open-source lidar andvisual simultaneous localization and mapping library for large-scaleand long-term online operation, Journal of Field Robotics, vol. 36,no. 2, pp. 416–446, 2019.
  * H. Xu, Y. Zhang, B. Zhou, L. Wang, X. Yao, G. Meng, and S. Shen,Omni-swarm: A decentralized omnidirectional visual–inertial–uwbstate estimation system for aerial swarms, Ieee transactions onrobotics, vol. 38, no. 6, pp. 3374–3394, 2022.
  * P. Yin, S. Zhao, H. Lai, R. Ge, J. Zhang, H. Choset, and S. Scherer,Automerge: A framework for map assembling and smoothing in city-scale environments, IEEE Transactions on Robotics, 2023.18
  * B. Mildenhall, P. P. Srinivasan, M. Tancik, J. T. Barron, R. Ramamoor-thi, and R. Ng, Nerf: Representing scenes as neural radiance fieldsfor view synthesis, Communications of the ACM, vol. 65, no. 1, pp.99–106, 2021.
  * B. Kerbl, G. Kopanas, T. Leimk ¨uhler, and G. Drettakis, 3d gaussiansplatting for real-time radiance field rendering, ACM Transactions onGraphics, vol. 42, no. 4, pp. 1–14, 2023.
  * Tesla, Inc., Autopilot support, 2023, accessed: 2023-03-30. 

<a id="lifelong"></a>
## D. Bio-Inspired and Lifelong Autonomy 
  * A. Witze et al., Nasa has launched the most ambitious mars roverever built: Here’s what happens next, Nature, vol. 584, no. 7819, pp.15–16, 2020.
  * L. Ding, R. Zhou, Y. Yuan, H. Yang, J. Li, T. Yu, C. Liu, J. Wang,S. Li, H. Gao, Z. Deng, N. Li, Z. Wang, Z. Gong, G. Liu, J. Xie,S. Wang, Z. Rong, D. Deng, X. Wang, S. Han, W. Wan, L. Richter,L. Huang, S. Gou, Z. Liu, H. Yu, Y. Jia, B. Chen, Z. Dang, K. Zhang,L. Li, X. He, S. Liu, and K. Di, A 2-year locomotive exploration andscientific investigation of the lunar farside by the yutu-2 rover, ScienceRobotics, vol. 7, no. 62, p. eabj6660, 2022.
  * G. D. Tipaldi, D. Meyer-Delius, and W. Burgard, Lifelong localizationin changing environments, The International Journal of RoboticsResearch, vol. 32, no. 14, pp. 1662–1678, 2013.
  * M. Zhao, X. Guo, L. Song, B. Qin, X. Shi, G. H. Lee, and G. Sun, Ageneral framework for lifelong localization and mapping in changingenvironment, in 2021 IEEE/RSJ International Conference on Intelli-gent Robots and Systems (IROS), 2021, pp. 3305–3312.
  * C. Chow and C. Liu, Approximating discrete probability distributionswith dependence trees, IEEE transactions on Information Theory,vol. 14, no. 3, pp. 462–467, 1968.
  * S. Zhu, X. Zhang, S. Guo, J. Li, and H. Liu, Lifelong localization insemi-dynamic environment, in 2021 IEEE International Conferenceon Robotics and Automation (ICRA), 2021, pp. 14 389–14 395.
  * M. Zaffar, S. Garg, M. Milford, J. Kooij, D. Flynn, K. McDonald-Maier, and S. Ehsan, VPR-bench: An open-source visual placerecognition evaluation framework with quantifiable viewpoint andappearance change, International Journal of Computer Vision., vol.129, no. 7, pp. 2136–2174, May 2021.
  * K. MacTavish, M. Paton, and T. D. Barfoot, Visual triage: A bag-of-words experience selector for long-term visual route following,in2017 IEEE International Conference on Robotics and Automation(ICRA), 2017, pp. 2065–2072.
  * A.-D. Doan, Y. Latif, T.-J. Chin, and I. Reid, Hm4: Hidden markovmodel with memory management for visual place recognition, IEEERobotics and Automation Letters, vol. 6, no. 1, pp. 167–174, 2021.
  * P. Yin, A. Abuduweili, S. Zhao, L. Xu, C. Liu, and S. Scherer,Bioslam: A bioinspired lifelong memory system for general placerecognition, IEEE Transactions on Robotics, 2023.
  * N. S ¨underhauf, P. Neubert, and P. Protzel, Are we there yet? challeng-ing seqslam on a 3000 km journey across all four seasons, in Proc. ofworkshop on long-term autonomy, IEEE international conference onrobotics and automation (ICRA), 2013, p. 2013.
  * A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, Vision meets robotics:The kitti dataset, The International Journal of Robotics Research,vol. 32, no. 11, pp. 1231–1237, 2013.20
  * W. Maddern, G. Pascoe, C. Linegar, and P. Newman, 1 year, 1000 km:The oxford robotcar dataset, The International Journal of RoboticsResearch, vol. 36, no. 1, pp. 3–15, 2017.
  * F. Warburg, S. Hauberg, M. Lopez-Antequera, P. Gargallo, Y. Kuang,and J. Civera, Mapillary street-level sequences: A dataset for lifelongplace recognition, in 2020 IEEE/CVF Conference on Computer Visionand Pattern Recognition (CVPR), 2020, pp. 2623–2632.
  * Y. Liao, J. Xie, and A. Geiger, KITTI-360: A novel dataset andbenchmarks for urban scene understanding in 2d and 3d, CoRR, vol.abs/2109.13410, 2021.
  * C. Ivan, P. Yin, J. Zhang, H. Choset, and S. Scherer, Alto: A large-scale dataset for uav visual place recognition and localization, arXivpreprint arXiv:2205.30737, 2022.
  * P. Yin, S. Zhao, R. Ge, I. Cisneros, R. Fu, J. Zhang, H. Choset,and S. Scherer, Alita: A large-scale incremental dataset for long-termautonomy, 2022.
  * D. Barnes, M. Gadd, P. Murcutt, P. Newman, and I. Posner, Theoxford radar robotcar dataset: A radar extension to the oxford robotcardataset, in 2020 IEEE International Conference on Robotics andAutomation (ICRA). IEEE, 2020, pp. 6433–6438.

<a id="development_tools"></a>
# Development Tools
<a id="dataset"></a>
## A. Public Datasets 
  * P. Yin, L. Xu, X. Li, C. Yin, Y. Li, R. A. Srivatsan, L. Li, J. Ji, andY. He, A multi-domain feature learning method for visual place recog-nition, in 2019 International Conference on Robotics and Automation(ICRA), 2019, pp. 319–324.
  * N. S ¨underhauf, P. Neubert, and P. Protzel, Are we there yet? challeng-ing seqslam on a 3000 km journey across all four seasons, in Proc. ofworkshop on long-term autonomy, IEEE international conference onrobotics and automation (ICRA), 2013, p. 2013.
  * F. Warburg, S. Hauberg, M. Lopez-Antequera, P. Gargallo, Y. Kuang,and J. Civera, Mapillary street-level sequences: A dataset for lifelongplace recognition, in 2020 IEEE/CVF Conference on Computer Visionand Pattern Recognition (CVPR), 2020, pp. 2623–2632.
  * C. Ivan, P. Yin, J. Zhang, H. Choset, and S. Scherer, Alto: A large-scale dataset for uav visual place recognition and localization, arXivpreprint arXiv:2205.30737, 2022.
  * K. Somasundaram, J. Dong, H. Tang, J. Straub, M. Yan, M. Goe-sele, J. J. Engel, R. De Nardi, and R. Newcombe, Project aria:A new tool for egocentric multi-modal ai research, arXiv preprintarXiv:2308.13561, 2023.
  * A. Geiger, P. Lenz, C. Stiller, and R. Urtasun, Vision meets robotics:The kitti dataset, The International Journal of Robotics Research,vol. 32, no. 11, pp. 1231–1237, 2013.20
  * W. Maddern, G. Pascoe, C. Linegar, and P. Newman, 1 year, 1000 km:The oxford robotcar dataset, The International Journal of RoboticsResearch, vol. 36, no. 1, pp. 3–15, 2017.
  * M. Ramezani, Y. Wang, M. Camurri, D. Wisth, M. Mattamala, andM. Fallon, The newer college dataset: Handheld lidar, inertial andvision with ground truth, in 2020 IEEE/RSJ International Conferenceon Intelligent Robots and Systems (IROS), 2020, pp. 4353–4360.
  * D. Barnes, M. Gadd, P. Murcutt, P. Newman, and I. Posner, Theoxford radar robotcar dataset: A radar extension to the oxford robotcardataset, in 2020 IEEE International Conference on Robotics andAutomation (ICRA). IEEE, 2020, pp. 6433–6438.
  * K. Burnett, D. J. Yoon, Y. Wu, A. Z. Li, H. Zhang, S. Lu, J. Qian,W.-K. Tseng, A. Lambert, K. Y. Leung et al., Boreas: A multi-seasonautonomous driving dataset, The International Journal of RoboticsResearch, vol. 42, no. 1-2, pp. 33–42, 2023.
  * M. Zaffar, S. Garg, M. Milford, J. Kooij, D. Flynn, K. McDonald-Maier, and S. Ehsan, VPR-bench: An open-source visual placerecognition evaluation framework with quantifiable viewpoint andappearance change, International Journal of Computer Vision., vol.129, no. 7, pp. 2136–2174, May 2021.
  * P. Yin, S. Zhao, R. Ge, I. Cisneros, R. Fu, J. Zhang, H. Choset,and S. Scherer, Alita: A large-scale incremental dataset for long-termautonomy, 2022.

<a id="libraries"></a>
## B. Supported Libraries 
  * B. Talbot, S. Garg, and M. Milford, Openseqslam2.0: An open sourcetoolbox for visual place recognition under changing conditions, in2018 IEEE/RSJ International Conference on Intelligent Robots andSystems (IROS), 2018, pp. 7758–7765.
  * M. Zaffar, S. Garg, M. Milford, J. Kooij, D. Flynn, K. McDonald-Maier, and S. Ehsan, Vpr-bench: An open-source visual place recogni-tion evaluation framework with quantifiable viewpoint and appearancechange, Int. J. Comput. Vision, vol. 129, no. 7, pp. 2136–2174, jul2021.
  * M. Humenberger, Y. Cabon, N. Guerin, J. Morat, V. Leroy, J. Revaud,P. Rerole, N. Pion, C. de Souza, and G. Csurka, Robust imageretrieval-based visual localization using kapture, 2020.


<!-- [25] R. Arandjelovic, P. Gronat, A. Torii, T. Pajdla, and J. Sivic, Netvlad:Cnn architecture for weakly supervised place recognition, in 2016IEEE Conference on Computer Vision and Pattern Recognition(CVPR), 2016, pp. 5297–5307.
[28] G. Berton, C. Masone, and B. Caputo, Rethinking visual geo-localization for large-scale applications, in Proceedings of theIEEE/CVF Conference on Computer Vision and Pattern Recognition,2022, pp. 4878–4888.
[82] A. Ali-Bey, B. Chaib-Draa, and P. Giguere, Mixvpr: Feature mixingfor visual place recognition, in Proceedings of the IEEE/CVF WinterConference on Applications of Computer Vision, 2023, pp. 2998–3007.
[93] Z. Fan, Z. Song, H. Liu, Z. Lu, J. He, and X. Du, Svt-net: Super light-weight sparse voxel transformer for large scale place recognition, inProceedings of the AAAI Conference on Artificial Intelligence, vol. 36,no. 1, 2022, pp. 551–560.
[29] R. Wang, Y. Shen, W. Zuo, S. Zhou, and N. Zheng, Transvpr:Transformer-based place recognition with multi-level attention aggre-gation, in Proceedings of the IEEE/CVF Conference on ComputerVision and Pattern Recognition, 2022, pp. 13 648–13 657.
[55] L. Luo, S. Zheng, Y. Li, Y. Fan, B. Yu, S.-Y. Cao, J. Li, and H.-L. Shen,Bevplace: Learning lidar-based place recognition using bird’s eye viewimages, in Proceedings of the IEEE/CVF International Conference onComputer Vision, 2023, pp. 8700–8709.
[52] K. Vidanapathirana, M. Ramezani, P. Moghadam, S. Sridharan, andC. Fookes, Logg3d-net: Locally guided global descriptor learning for3d place recognition, in 2022 International Conference on Roboticsand Automation (ICRA), 2022, pp. 2215–2221.
[50] J. Komorowski, Minkloc3d: Point cloud based large-scale place recog-nition, in 2021 IEEE Winter Conference on Applications of ComputerVision (WACV), 2021, pp. 1789–1798.
[45] M. A. Uy and G. H. Lee, Pointnetvlad: Deep point cloud basedretrieval for large-scale place recognition, in 2018 IEEE/CVF Con-ference on Computer Vision and Pattern Recognition, 2018, pp. 4470–4479.
[35] J. Komorowski, M. Wysoczanska, and T. Trzcinski, Minkloc++:lidar and monocular image fusion for place recognition, in 2021International Joint Conference on Neural Networks (IJCNN). IEEE,2021, pp. 1–8.
 -->
