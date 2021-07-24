$(document).on("ready", function () {
  const user_id = $(".userid").attr("id");
  getInboxPageData(user_id);
});

const getInboxPageData = async (user_id) => {
  const [notificationsData, notificationsError] = await getNotifications(
    user_id
  );
  if (!notificationsError) {
    await drawNotifications(notificationsData);
  }

  const [messageRoomsData, messageRoomsError] = await getMessageRooms(user_id);
  if (!messageRoomsError) {
    await drawMessageRooms(messageRoomsData, user_id);
  }
};

const getNotifications = async (user_id) => {
  try {
    const data = await postData("/profile/get-user-notifications/", {
      user_id: user_id,
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const getMessageRooms = async (user_id) => {
  try {
    const data = await postData("/profile/get-message-rooms/", {
      user_id: user_id,
    });
    return [data.items, null];
  } catch (error) {
    return [null, error];
  }
};

const drawNotifications = async (data) => {
  var notifications = [];
  console.log(data);
  $.each(data, function (key, val) {
    notifications.push(`<div class="notification notification-${val.notification.color}" onclick="javascript: navigate('/article/${val.notification.article_id}')" id=${val.id}>
      <i class="${val.notification.icon}"></i>
      <span>
        <strong onclick="javascript: navigate('/article/${val.notification.user_id}')" >
          ${val.notification.username} 
        </strong>
        ${val.notification.message}
      </span>
    </div>`);
  });
  $(".notifications").append(notifications.join(""));
};

const drawMessageRooms = async (data, user_id) => {
  var messageRooms = [];
  console.log(data);
  $.each(data, function (key, val) {
    messageRooms.push(`<div class="room-row" id=${val.id}>
      <img src=${
        val.u1_id == user_id
          ? `${val.u2_profile_image}`
          : `${val.u1_profile_image}`
      } />
      <strong>${
        val.u1_id == user_id ? `${val.u2_username}` : `${val.u1_username}`
      }</strong>
    </div>`);
  });
  $(".message-rooms").append(messageRooms.join(""));
  if (is_unread === true && unread_user == user_id) {
    $(`.room-row#${id}`).addClass("unread");
  }
};

const getMessages = (room_id) => {
  postData("/profile/get-messages/", {
    room_id: room_id,
  }).then((response) => {
    console.log(response);
  });
};
