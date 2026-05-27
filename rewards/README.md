# rewards split 구조

권장 조회 순서:

1. `rewards/index.json`
   - 얇은 색인 파일.
   - 보스 목록, 아이템 요약, 드랍테이블 요약, 상세 파일 경로만 가진다.

2. `rewards/by-boss/{bossId}.json`
   - 특정 보스의 보상 아이템과 드랍테이블을 한 번에 볼 때 사용한다.

3. `rewards/items/{itemId}.json`
   - 특정 아이템의 상세 설명, 효과, rawBlock, 유물 스킬 등을 볼 때 사용한다.

4. `rewards/drop-tables/{dropTableId}.json`
   - 특정 드랍테이블 상세만 필요할 때 사용한다.

기존 `rewards.json`처럼 전체를 한 번에 가져오지 말고,
항상 index -> 필요한 상세 파일 순서로 가져오는 것을 권장한다.
