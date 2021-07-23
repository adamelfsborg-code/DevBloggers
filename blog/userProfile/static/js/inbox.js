$(document).on("ready", function () {
  const user_id = $(".userid").attr("id");
  getNotifications(user_id);
  getMessageRooms(user_id);
});

const getNotifications = (user_id) => {
  postData("/profile/get-user-notifications/", {
    user_id: user_id,
  }).then((response) => {
    if (response.msg === "200") {
      console.log(response.items);
      $.each(response.items, function (key, val) {
        drawNotification(
          val.id,
          val.notification.message,
          val.notification.article_id,
          val.notification.username,
          val.notification.user_id,
          val.notification.icon,
          val.notification.color
        );
      });
    }
  });
};

const getMessageRooms = async (user_id) => {
  postData("/profile/get-message-rooms/", {
    user_id: user_id,
  }).then((response) => {
    console.log(response);
    if (response.msg === "200") {
      $.each(response.items, async function (key, val) {
        await drawMessageRooms(
          user_id,
          val.id,
          val.u1_id,
          val.u2_id,
          val.u1_username,
          val.u2_username,
          val.u1_profile_image,
          val.u2_profile_image,
          val.is_unread,
          val.unread_user
        );
      });
    }
  });
};

const getMessages = (room_id) => {
  postData("/profile/get-messages/", {
    room_id: room_id,
  }).then((response) => {
    console.log(response);
  });
};

const drawNotification = (
  id,
  msg,
  article_id,
  username,
  user_id,
  icon,
  color
) => {
  const widget = `<div class="notification notification-${color}" onclick="javascript: navigate('/article/${article_id}')" id=${id}></div>`;
  const iconType = `<i class="${icon}"></i>`;
  const message = `<span><strong onclick="javascript: navigate('/article/${user_id}')" >${username} </strong>${msg}</span>`;

  $(".notifications").append(widget);
  $(`.notification#${id}`).append(iconType);
  $(`.notification#${id}`).append(message);
};

const drawMessageRooms = (
  user_id,
  id,
  u1_id,
  u2_id,
  username1,
  username2,
  profile_img1,
  profile_img2,
  is_unread,
  unread_user
) => {
  const row = `<div class="room-row" id=${id}></div>`;
  var image, name;
  if (u1_id == user_id) {
    image = `<img src=${
      profile_img2 !== null ? profile_img2 : "/static/img/default.jpg"
    } />`;
    name = `<strong>${username2}</strong>`;
  } else {
    image = `<img src=${
      profile_img1 !== null ? profile_img1 : "/static/img/default.jpg"
    } />`;
    name = `<strong>${username1}</strong>`;
  }
  $(".message-rooms").append(row);
  $(`.room-row#${id}`).append(image);
  $(`.room-row#${id}`).append(name);

  if (is_unread === true && unread_user == user_id) {
    $(`.room-row#${id}`).addClass("unread");
  }
};
