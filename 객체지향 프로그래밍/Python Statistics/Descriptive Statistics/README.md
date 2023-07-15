# Descriptive Statistics

### 기술통계(Descriptive Statistics)

* 통계 : 데이터를 수집 및 정리하여 <span style="color:blue">특징을 확인</span>하는 것
  * 통계학에서 최종적으로 알고 싶은 것 -> <span style = "color:red">모집단의 특징</span>
  * 특징 : "<span style="color:blue">중심화 경향치</span>" vs "<span style="color:blue">산포도</span>"
* 모집단의 특징을 알기 위해 데이터를 수집, 분석, 시각화
  * 특정 집단에 관한 현상을 <span style="color:purple">수학적으로 연산</span>하여 기술
  * 특징을 기술(설명)할 수 있으면 <span style="color:purple">어떤 사실을 객관적으로 표현</span> 가능
* 하나의 수치로 결론을 내릴 순 없지만 결론을 향한 기반을 제공



### 기술통계(Descriptive Statistics) - 변수와 척도

* 통계 변수
  * 명명(Norminal) : 측정값의 같고 다름만 확인, 측정값 사이에 순서 없음
  * 서열(Ordinal) : 측정값 사이에 순서가 있지만, 간격이 동일하지 않음
  * 등간(Interval) : 측정값 사이에 순서가 있고, 간격이 동일/영점(0)의 의미 임의적
  * 비율(Ratio) : 절대영점(아무것도 존재하지 않는 상태) 존재/사칙연산 모두 가능

![image-20230715192105531](C:\Users\ehddn\AppData\Roaming\Typora\typora-user-images\image-20230715192105531.png)



### 기술통계(Descriptive Statistics) - 중심화 경향치

* <span style="color:blue">중심화 경향치(Measure of Central Tendency</span>
  * 집단을 <span style="color:blue">대표</span>하는 값(무엇을 중심으로 모여 있는가?)<br/>EX) 평균(mean), 중앙값(median), 최빈값(mode)
* <span style ="color:red">평균</span> : 전체 데이터를 더한 다음 데이터의 개수로 나눠준 값
  * 이상치(outlier) : 평균에 급격하게 영향을 주는 것
* <span style ="color:red">중앙값</span> : 전체 데이터를 크기 순서로 정렬하여 순서상 중앙에 위치한 값
* <span style ="color:red">최빈값</span> : 전체 데이터에서 가장 빈번하게 관찰된 값



### 기술통계(Descriptive Statistics) - 산포도

* <span style ="color:blue">산포도</span>(Degree of Dispersion)
  * 집단 내 데이터가 <span style ="color:blue">흩어져 있는 정도</span><br/>EX) 범위(range), 사분위범위(Interquartile range), <span style ="color:red">분산</span>, <span style ="color:red">표준편차</span>
* <span style ="color:red">범위</span> : 수치형 연속변수 값의 최솟값과 최댓값의 사이의 거리
  * 범위 = 최댓값 - 최솟값
  * 이상치(outlier)를 포함
* <span style ="color:red">최솟값</span>(Q1 - 1.5 * IQR)과 <span style ="color:red">최댓값</span>(Q3 + 1.5 * IQR)
* <span style ="color:red">사분위범위</span> : 0%, 25%,50%, 75%, 100% 구간으로 나눈 <span style ="color:purple">사분위수에서 25% 75% 사이</span>의 값들(boxplot으로 표현)

![image-20230715192920711](C:\Users\ehddn\AppData\Roaming\Typora\typora-user-images\image-20230715192920711.png)

* 분산(variance/<span style="color:red">var</span>)

  * 편찻값(관측치 - 평균)의 <span style="color:red">제곱</span>의 합을 데이터의 수로 나눈 값

    ![image-20230715193222806](C:\Users\ehddn\AppData\Roaming\Typora\typora-user-images\image-20230715193222806.png)

  * 편찻값으로는 <span style="color:blue">흩어진 정도</span>를 조사할 수 없음(음수, 양수가 각각 상쇄)

  * 따라서 <span style="color:red">편찻값을 제곱</span>의 평균으로 계산

* 관측치들이 <span style="color:blue">평균에서 평균적으로 얼마나 떨어져 있는지</span> 확인

  * <span style="color:maroon">단점</span> : 값이 너무 커짐(제곱 값)

* 표준편차(standard deviation/<span style="color:red">std</span>)

  * 표준편차는 분산의 <span style="color:blue">양의 제곱근</span>

  * 분산에 루트를 적용하여 계산

    ![image-20230715193453389](C:\Users\ehddn\AppData\Roaming\Typora\typora-user-images\image-20230715193453389.png)

    

